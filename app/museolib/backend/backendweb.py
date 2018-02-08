from museolib.backend import Backend
from kivy.logger import Logger
from kivy.network.urlrequest import UrlRequest
from functools import partial
from urllib import unquote_plus, urlopen
    
class BackendWeb(Backend):

    def __init__(self, **kwargs):
        super(BackendWeb, self).__init__(**kwargs)
        self.expo = None
        self.url = kwargs.get('url')
        self.data_url = kwargs.get('data_url')

    def set_expo(self, uid):
        self.expo = uid

    def build_url(self, path):        
        return self.url + path

    def build_data_url(self, path):
        return self.data_url + path

    def unquote_json(self, on_success, on_error, req, json):
        try:
            json = self._unquote(json)
            on_success(req, json)
        except Exception, e:
            Logger.exception('error on request %r' % req, json)
            on_error(req, e)

    def _unquote(self, json):
        unquote = self._unquote
        tp = type(json)
        if tp in (list, tuple):
            return tp([unquote(x) for x in json])
        elif tp is dict:
            return dict((x, unquote(y)) for x, y in json.iteritems())
        elif tp in (str, unicode):
            json = unquote_plus(json)
            try:
                ojson = json
                json = json.encode('latin1')
                json = json.decode('utf8')
            except Exception, e:
                print 'error on string %r' % json
                print 'unable to decode ?', e
                json = ojson
        return json

    def load_items(self, on_success=None, on_error=None):
        return []

    def _filter_on_id(self, uid, on_success, on_error, req, json):
        try:
            data = [x for x in json if str(x['id']) == str(uid)]
            if data:
                data = data[0]
            on_success(req, data)
        except Exception, e:
            Logger.exception('error on request %r' % req)
            on_error(req, e)

    #
    # Public
    #

    def get_expos(self, uid=None, on_success=None, on_error=None, on_progress=None):
        url = self.build_url('')
        on_success = partial(self.unquote_json, on_success, on_error)
        if uid:
            on_success = partial(self._filter_on_id, uid, on_success, on_error)
        Logger.debug('BackendWeb: GET %r' % url)
        self.req = UrlRequest(url, on_success=on_success, on_error=on_error, on_progress=on_progress, timeout=2)

    def get_objects(self, on_success=None, on_error=None, on_progress=None):
        assert(self.expo is not None)
        url = self.build_url('?act=expo&id=%s' % self.expo)
        on_success = partial(self.unquote_json, on_success, on_error)
        Logger.debug('BackendWeb: GET %r' % url)
        self.req = UrlRequest(url, on_success=on_success, on_error=on_error, on_progress=on_progress)

    def get_file(self, filename, on_success=None, on_error=None, on_progress=None):
        Logger.debug('BackendWeb: GET %r' % filename)
        self.req = UrlRequest(filename, on_success=on_success, on_error=on_error, on_progress=on_progress)

    def download_object(self, uid, directory, extension, on_success=None, on_error=None,
            on_progress=None):
        # 2 cases to handle
        # raw images are in objets/raw/*.png
        # compressed images are dispatched in multiple folder like
        # - objets/compressed/dds/*.dds
        # - ...
        if directory != 'raw':
            directory = 'compressed/%s' % directory
        url = self.build_data_url('objets/%(uid)s/%(directory)s/%(uid)s.%(ext)s'
                % {'uid': uid, 'directory': directory, 'ext': extension})

        resource = urlopen(url)
        status = resource.getcode()
        if status == 404 and extension == 'jpg':
            url = self.build_data_url('objets/%(uid)s/%(directory)s/%(uid)s.%(ext)s'
                % {'uid': uid, 'directory': directory, 'ext': 'png'})

        Logger.debug('BackendWeb: GET %r' % url)
        self.req = UrlRequest(url, on_success=on_success, on_error=on_error, on_failure=on_error, on_progress=on_progress, timeout=5,
                    chunk_size=32768)



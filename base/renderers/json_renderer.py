import json
from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Custom logic here
        # You can modify the data or perform any additional processing
        return super().render(data, accepted_media_type, renderer_context)

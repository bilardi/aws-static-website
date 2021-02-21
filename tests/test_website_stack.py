from aws_cdk import core
from aws_static_website.website_stack import WebsiteStack
from aws_cdk_test_synth.test_synth import TestSynth

class TestWebsiteStack(TestSynth):
    def __init__(self, *args, **kwargs):
        TestSynth.__init__(self, 'tests/website_stack.yaml', *args, **kwargs)

    def synth(self, app):
        WebsiteStack(app, 
            id="test",
            bucket_name="bucket.domain.name",
            website_params={
                "index_document": "index.html",
                "error_document": "index.html"
            },
            aliases=["bucket.domain.name"],
            acm_certificate_arn="",
            hosted_params={
                "zone_name": "domain.name",
#                "zone_id": "Z2FDTNDATAQYW2"
            }
        )

if __name__ == '__main__':
    unittest.main()

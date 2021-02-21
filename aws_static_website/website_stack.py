"""The class for managing your AWS static website

The class requires the follow properties:
    'id' (str): the name of project used for the prefix of the stack name
    'bucket_name' (str): the name of bucket and domain
    'website_params' (dict): the dictionary of the Website custom parameters
        'index_document' (str): the index file name
        'error_document' (str): the error file name
    'aliases' (list): the list of domain names
    'acm_certificate_arn' (str): the arn of ACM certificate
    'hosted_params' 
        'zone_name' (str): the hosted zone name
        'zone_id' (str): the hosted zone identifier

All properties are mandatory, except zone_id if you need to create a new Host Zone.
Here's an example:

    >>> from aws_cdk import core
    >>> from aws_static_website.website_stack import WebsiteStack
    >>> app = core.App()
    >>> WebsiteStack(app,
    >>>     id="aws-static-website",
    >>>     bucket_name="bucket.domain.name",
    >>>     website_params=website_params,
    >>>     aliases=["bucket.domain.name"],
    >>>     acm_certificate_arn="",
    >>>     hosted_params=hosted_params
    >>> )
    >>> app.synth()

# license MIT
# support https://github.com/bilardi/aws-static-website/issues
"""
from aws_cdk import (core, aws_s3 as s3, aws_iam as iam)

class WebsiteStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, bucket_name: str=None, aliases: list=None, hosted_params: dict=None, acm_certificate_arn: str=None, website_params: dict=None, **kwargs) -> None:
        """
        deploys all AWS resources for your static website
            Resources:
                AWS::S3::Bucket for your website
                AWS::S3::BucketPolicy with read-only policy
        """
        super().__init__(scope, id, **kwargs)

        stage = ''
        if scope.node.try_get_context("stage"):
            stage = scope.node.try_get_context("stage") + '-'

        website_bucket = s3.Bucket(self, id+"Bucket",
            bucket_name=stage+bucket_name,
            access_control=s3.BucketAccessControl('PUBLIC_READ'),
            website_index_document=website_params['index_document'],
            website_error_document=website_params['error_document']
        )

        policy_document = iam.PolicyDocument()
        policy_statement = iam.PolicyStatement(
            actions=["s3:GetObject"],
            effect=iam.Effect("ALLOW"),
            resources=[website_bucket.bucket_arn + "/*"]
        )
        policy_statement.add_any_principal()
        policy_document.add_statements(policy_statement)

        bucket_policy = s3.CfnBucketPolicy(self, id+"Policy",
            bucket=website_bucket.bucket_name,
            policy_document=policy_document
        )
Usage
=====

The **aws_static_website** package deploys the resources by the file named **app.py** file, where you have to initialize its WebsiteStack class.

You can manage all configuration that you need, directly in the **app.py** file.

Example
#######

You have chosen the domain name named **domain.name** and your subname will be **bucket**:
your ``bucket`` has to be named **bucket.domain.name**.

Only S3 and Cloudfront
**********************

If you want to use the url provided from S3 service, you only have to configure the ``index_document`` and ``error_document`` properties

.. code-block:: bash

    project_name = "aws-static-website"
    website_params = {
        "index_document": "index.html",
        "error_document": "index.html"
    }

    app = core.App()
    WebsiteStack(app, 
        id=project_name,
        bucket_name="bucket.domain.name",
        website_params=website_params
    )

You can find a `complete example <https://github.com/bilardi/aws-static-website/tree/master/app.py>`_ in this repo.

Even DNS
********

If you want to use the url **bucket.domain.name**, you also have to configure the hosted zone:

* you can pass the hosted both ``zone_name`` and ``zone_id``, and the package will only deploy the **DNS record type A**

.. code-block:: bash

    project_name = "aws-static-website"
    website_params = {
        "index_document": "index.html",
        "error_document": "index.html"
    }
    hosted_params = {
        "zone_name": "domain.name",
        "zone_id": "Z23ABC4XYZL05B"
    }

    app = core.App()
    WebsiteStack(app, 
        id=project_name,
        bucket_name="bucket.domain.name",
        website_params=website_params,
        hosted_params=hosted_params
    )

* or you can only pass the hosted ``zone_name``, and the package will deploy the **Hosted Zone** and the **DNS record type A**

.. code-block:: bash

    project_name = "aws-static-website"
    website_params = {
        "index_document": "index.html",
        "error_document": "index.html"
    }
    hosted_params = {
        "zone_name": "domain.name"
    }

    app = core.App()
    WebsiteStack(app, 
        id=project_name,
        bucket_name="bucket.domain.name",
        website_params=website_params,
        hosted_params=hosted_params
    )

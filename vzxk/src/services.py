def get_product_image_upload_path(instance, file):
    return f'product/picture/{instance.id}/{file}'

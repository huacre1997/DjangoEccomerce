# from celery import  task
# from easy_thumbnails.files import generate_all_aliases

# @task
# def generate_thumbnails(model, pk, field):
#     instance = model._default_manager.get(pk=pk)
#     fieldfile = getattr(instance, field)
#     generate_all_aliases(fieldfile, include_global=True)
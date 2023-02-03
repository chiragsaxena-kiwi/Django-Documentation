from celery import shared_task



@shared_task

def conver_doc_to_pdf(myfile):
    
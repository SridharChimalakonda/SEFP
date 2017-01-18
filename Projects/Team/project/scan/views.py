from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from .tasks import scan
import time

# Create your views here.

def poll_state(request):
    """ A view to report the progress to the user """
    data = 'Fail'
    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            task = AsyncResult(task_id)
            data = task.result or task.state
        else:
            data = 'No task_id in the request'
    else:
        data = 'This is not an ajax request'

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def home(request):
	context = {
	}
	return render(request, 'quickscan_index.html', context)

def scanner(request):
	"""if request.method == 'GET':
		job_id = request.GET['task_id']
		job = AsyncResult(job_id)
		data = job.result or job.state
		context = {
			'data': data,
			'job_id': job_id,
		}
		return HttpResponse(json.dumps(context), content_type='application/json')"""

	if request.method == 'POST':
		url = request.POST.get('url', None)
		job = scan.delay(url)
		return HttpResponse(json.dumps({'job':job.id}), content_type='application/json')
		"""url = request.POST.get('url', None)
		#url = url
		sqlR = SQLInjection()
		xssR = XSS()

		progress1 = sqlR.scan(url)
		progress2 = xssR.scan(url)
		#print(progress)
		#progress = 0
		statusdict = {'url':url, 'progress1':progress1, 'progress2':progress2}
		return HttpResponse(json.dumps(statusdict), content_type='application/json')"""
		#return stream_response(request)
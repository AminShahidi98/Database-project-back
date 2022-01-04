from django.shortcuts import render
from .models import Violation

# Create your views here.
def showViolationsListAsc(response):
    temp = Violation.objects.all()
    violations = []
    for v in temp:
        violations.append(v)
    violations.sort(key=lambda x: x.Amount, reverse=False)
    return render(response, "violations/list.html", {"violations":violations, "title":"تخلفات - افزایشی"})

def showViolationsListDec(response):
    temp = Violation.objects.all()
    violations = []
    for v in temp:
        violations.append(v)
    violations.sort(key=lambda x: x.Amount, reverse=True)
    return render(response, "violations/list.html", {"violations":violations, "title":"تخلفات - کاهشی"})
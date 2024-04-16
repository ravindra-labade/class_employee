from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.views import View


class create_view(View):
    def get(self, request):
        form = EmployeeForm()
        context = {'form': form}
        return render(request, 'emp/create.html', context)

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        context = {'form': form}
        return render(request, 'emp/create.html', context)


class show_view(View):
    def get(self, request):
        employees = Employee.objects.all()
        context = {'employees': employees}
        return render(request, 'emp/show.html', context)


class update_view(View):
    def get(self, request, pk):
        obj = Employee.objects.get(id=pk)
        form = EmployeeForm(instance=obj)
        context = {'form': form}
        return render(request, 'emp/create.html', context)

    def post(self, request, pk):
        obj = Employee.objects.get(id=pk)
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')


class delete_view(View):
    def get(self, request, pk):
        return render(request, 'emp/confirm.html')

    def post(self, pk):
        obj = Employee.objects.get(id=pk)
        obj.delete()
        return redirect('show_url')
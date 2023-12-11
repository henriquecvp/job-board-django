from django.shortcuts import render, redirect
from .models import Job, JobApplication
from .forms import JobForm, ApplicationForm
from django.contrib import messages

def job_list(request):
    # verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('Login')
    
    # renderiza vagas para o candidato e vagas próprias para empresas
    if request.user.company:
        jobs = Job.objects.filter(owner=request.user.username)
    else:
        jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})
    

def create_job(request):
    # abre o formulário para criar vagas e salva ele
    if request.user.company and request.user.is_authenticated:
        if request.method == 'POST':
            form = JobForm(request.POST)
            if form.is_valid():
                job = form.save(commit=False)
                job.company = request.user.first_name
                job.owner = request.user.username
                job.save()
                messages.success(request, 'Sucesso!')
                return redirect('job_list')
        else:
            form = JobForm()
        return render(request, 'job_create.html', {'form': form})
    else:
        messages.error(request, 'Erro!')
        return redirect('job_list')
    
def edit_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('Login')
    # filta o objeto Job específico
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return redirect('job_list')
    
    if request.user.username != job.owner:
        return redirect('job_list')


    # abre o formulário já com as informações da vaga para alteração
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)

    return render(request, 'job_edit.html', {'form': form, 'job': job})
    
def delete_job(request, job_id):

    if not request.user.is_authenticated:
        return redirect('Login')
    
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return redirect('job_list')
    
    # deleta se o usuário é o dono
    if request.user.username == job.owner:
        job.delete()

    return redirect('job_list')

def apply_for_job(request, job_id):

    if not request.user.is_authenticated:
        return redirect('Login')
    
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return redirect('job_list')
    
    # garante que o usuário não é uma empresa e a singularidade da candidatura
    if request.user.company or JobApplication.objects.filter(job_opening=job, applicant=request.user).exists():
        return redirect('job_list')
    
    # abre o formulário de aplicação e salva ele
    if request.method == 'POST':
            form = ApplicationForm(request.POST)
            if form.is_valid():
                appl = form.save(commit=False)
                appl.applicant_id = request.user
                appl.applicant_email = request.user.username
                appl.applicant_first_name = request.user.first_name
                appl.job_opening_id = job
                appl.appplicant_match = 0

                #pontuar 'match' do candidato
                if appl.applicant_salary_expec <= 1000 :
                    salary_range = 1
                elif 1000 < appl.applicant_salary_expec <= 2000:
                    salary_range = 2
                elif 2000 < appl.applicant_salary_expec <= 3000:
                    salary_range = 3
                else: 
                    salary_range = 4

                if salary_range <= int(job.salary): appl.appplicant_match += 1
                if appl.applicant_ed_level >= job.ed_level: appl.appplicant_match += 1

                appl.save()

                # contador de número de cadidaturas para visialização
                job.applicants_count += 1
                job.save()

                messages.success(request, 'Sucesso!')
                return redirect('job_list')
    else:
        form = ApplicationForm()
        return render(request, 'job_apply.html', {'form': form,  'job': job})
    

def job_detail(request, job_id):

    if not request.user.is_authenticated:
        return redirect('Login')
    
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return redirect('job_list')
    
    # busca e lista as candidaturas de uma vaga para seu dono
    if request.user.username == job.owner:
        appl = JobApplication.objects.filter(job_opening=job)
        return render(request, 'job_detail.html', {'job': job, 'applications': appl})
    
    else:
        return redirect('job_list')


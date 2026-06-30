from django.shortcuts import render, redirect
from .models import Note
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    
    search_query = request.GET.get('search', '')

    notes = Note.objects.all()

    if search_query:
        notes = notes.filter(
            subject__icontains=search_query
        )


    return render(
        request,
        'home.html',
        {
            'notes': notes
        } 
    )
@login_required
def upload_note(request):

    if request.method == "POST":

        title = request.POST['title']
        subject = request.POST['subject']
        semester = request.POST['semester']
        description = request.POST['description']
        pdf = request.FILES.get('pdf')

        Note.objects.create(
            owner=request.user,
            title=title,
            subject=subject,
            semester=semester,
            description=description,
            pdf=pdf
            )

        return redirect('home')

    return render(request, 'upload_note.html')

@login_required
def delete_note(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id
    )

    if request.user != note.owner and not request.user.is_superuser:
        return redirect('home')

    note.delete()

    return redirect('home')

@login_required
def edit_note(request, note_id):

    note = get_object_or_404(
    Note,
    id=note_id
    )
    if request.user != note.owner and not request.user.is_superuser:
        return HttpResponse("Permission Denied")

    if request.method == "POST":

        note.title = request.POST['title']
        note.subject = request.POST['subject']
        note.semester = request.POST['semester']
        note.description = request.POST['description']

        note.save()

        return redirect('home')

    return render(
        request,
        'edit_note.html',
        {'note': note}
    )

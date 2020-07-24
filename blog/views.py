from django.http import HttpResponse, HttpResponseRedirect, Http404, FileResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.db.models.functions import Trunc
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage, default_storage

from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

from PIL import Image as imge
from io import BytesIO

from string import digits

import datetime

from .forms import ImageForm
from .models import Blogpost, Source, Image

def index(request):

    context = {
        "Blogposts" : Blogpost.objects.all().order_by('-date_posted')
    }

    return render(request, "blog/index.html", context)

def post(request, Blogpost_id):

    if request.method == "GET":

        try:
            post = Blogpost.objects.get(pk=Blogpost_id)
            
        except Blogpost.DoesNotExist:
            raise Http404("This post does not exist")

        context ={
            "Blogpost" : Blogpost.objects.get(pk=Blogpost_id),
            "Sources" : Source.objects.filter(blogpost = Blogpost_id)
        }
        
        return render(request, "blog/post.html", context)

    if request.method == "POST":

        if request.POST.get("sourceLink") and request.POST.get("sourceTitle"):

            blogpost = Blogpost.objects.get(pk=Blogpost_id)
            source = Source()
            source.link = request.POST.get('sourceLink')
            source.title = request.POST.get('sourceTitle')
            source.blogpost = blogpost
            source.save()
            
        return HttpResponseRedirect(request.path_info)

def motivateur(request):

    return render(request, "blog/motivateur.html")

def generator(request):

    if request.method == "POST":

        # Set the user inputs vars
        name = str(request.POST.get('name'))
        adress = str(request.POST.get('adress'))
        city = str(request.POST.get('city'))
        mail = str(request.POST.get('mail'))
        phone = str(request.POST.get('phone'))
        job = "Objet: Candidature au poste de \"{}\"".format(str(request.POST.get('job')))
        diploma = str(request.POST.get('diploma'))
        school = str(request.POST.get('school'))
        comp1 = str(request.POST.get('comp1'))
        comp2 = str(request.POST.get('comp2'))
        comp3 = str(request.POST.get('comp3'))

        # Set date and place and contact

        remove_digits = str.maketrans('', '', digits)
        place = city.translate(remove_digits)
        place = place.strip()
        today = datetime.date.today()
        dateplace =  "À " + place + " le " + str(today.day) + "/" + str(today.month) + "/" + str(today.year)
        contact = "Madame, Monsieur,"
        end = contact

        # If there is text in the contact field
        if len(str(request.POST.get('contact'))) != 0 : 
            contact = "à l'attention de " + str(request.POST.get('contact')) + ","
            end = str(request.POST.get('contact')) + ","

        # Generate the pdf
        doc = SimpleDocTemplate("/tmp/somefilename.pdf", rightMargin=2*cm,leftMargin=2*cm,topMargin=2*cm,bottomMargin=2*cm)
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
        letter = []

        # Write the pdf with differents strings and inputs 
        ptext = '<font size="12">{}</font>'.format(name)
        letter.append(Paragraph(ptext, styles["Normal"]))  
        ptext = '<font size="12">{}</font>'.format(adress)
        letter.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size="12">{}</font>'.format(city)
        letter.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size="12">{}</font>'.format(mail)
        letter.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size="12">{}</font>'.format(phone)
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 50))
        ptext = '<font size="12">{}</font>'.format(dateplace)
        letter.append(Paragraph(ptext, styles["Right"])) 
        letter.append(Spacer(1, 80))
        ptext = '<font size="12">{}</font>'.format(job)
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 50))
        ptext = '<font size="12">{}</font>'.format(contact)
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">Ayant récemment obtenu mon diplôme de {} à {}, je suis désormais à la recherche d\'un emploi.</font>'.format(diploma, school)
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">J\'ai, durant mon cursus scolaire et professionnel, pu acquérir de nombreuses compétences en {} mais aussi en {} ou encore en {}. Ces différentes expériences m\'ont permis d\'obtenir mes premiers savoirs et je pense désormais être en mesure de pouvoir candidater pour le poste que vous proposez aujourd\'hui.</font>'.format(comp1, comp2, comp3)
        letter.append(Paragraph(ptext, styles["Normal"])) 
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">Comme vous avez également pu le remarquer durant la lecture de mon curriculum vitae j\'ai aussi pu développer durant cette période plusieurs compétences annexes  sur mon temps personnel, qui, je pense, peuvent entrer en complémentarité avec les qualités requise pour occuper ce poste.</font>'
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">De plus, je trouve le fait de travailler pour une organisation d\'envergure comme la vôtre peut être extrêmement enrichissant tant professionnellement que personnellement.</font>'
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">Appliqué, honnête et sociable, je souhaite occuper ce poste avec tout le sérieux et l\'enthousiasme dont dont j\'ai déjà pu faire preuve  durant la poursuite de mes études. De plus, mes capacités d’adaptation me permettent de m’intégrer très rapidement au sein d’une équipe de travail.</font>'
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">Je reste à votre disposition pour toute information complémentaire, ou pour vous rencontrer lors d’un entretien.</font>'
        letter.append(Paragraph(ptext, styles["Normal"]))  
        letter.append(Spacer(1, 15))
        ptext = '<font size="12">Veuillez agréer, {} l’expression de mes sincères salutations.</font>'.format(end)
        letter.append(Paragraph(ptext, styles["Normal"]))
        letter.append(Spacer(1, 30))
        ptext = '<font size="12">{}</font>'.format(name)
        letter.append(Paragraph(ptext, styles["Center"]))  
        
        # Build the pdf
        doc.build(letter)
    
        fs = FileSystemStorage("/tmp")
        with fs.open("somefilename.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Lettre.pdf"'
            return response

        return response
    else:

        return render(request, "blog/motivateur.html")

def scrambbler(request):

    if request.method == "POST": 
        
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid() :
            
            form.save()
            
            img = form.instance.picture
            name = form.instance.name

            input = imge.open(img)
            temp = imge.new("RGB", input.size)
            output = imge.new("RGB", input.size)
            
            for x in range(0, input.width, 200):
                col1 = input.crop((x, 0, x + 100, input.height))

                if (x + 200) <= input.width:
                    col2 = input.crop((x + 100, 0, x + 200, input.height))
                    temp.paste(col1, (x + 100, 0))
                    temp.paste(col2, (x, 0))
                else:
                    col2 = input.crop((x + 100, 0, input.width, input.height))
                    temp.paste(col1, (x, 0))
                    temp.paste(col2, (x + 100, 0))

            for y in range(0, temp.height, 200):

                row1 = temp.crop((0, y, temp.width, y + 100))
                
                if (y + 200) <= temp.height:
                    row2 = temp.crop((0, y + 100, temp.width, y + 200))
                    output.paste(row1, (0, y + 100))
                    output.paste(row2, (0, y))
                else:
                    row2 = temp.crop((y + 100, 0, temp.height, temp.width))
                    row2 = temp.crop((0, y + 100, temp.width, temp.height))
                    output.paste(row1, (0, y))
                    output.paste(row2, (0, y + 100))

            buffer = BytesIO()
            output.save(buffer, format = 'PNG')
            buffer.seek(0)

            return FileResponse(buffer, as_attachment=True, filename=(name + ".png"))

        return render(request, "blog/scrambbler.html", {'form': form})

    else:
        form = ImageForm()
        return render(request, "blog/scrambbler.html", {'form': form})

@login_required
def delete(request, Blogpost_id):
    post = Blogpost.objects.get(pk=Blogpost_id)
    post.delete()
    messages.success(request, 'Post deleted')
    return redirect('/')

@login_required
def deleteSource(request, Blogpost_id, Source_id):

    source = Source.objects.filter(blogpost = Blogpost_id, id = Source_id)
    source.delete()

    return redirect(sources, Blogpost_id=Blogpost_id)

@login_required
def sources(request, Blogpost_id):

    context ={
        "Blogpost" : Blogpost.objects.get(pk=Blogpost_id),
        "Sources" : Source.objects.filter(blogpost = Blogpost_id)
    }

    if request.method == "POST":

        if request.POST.get("sourceLink") and request.POST.get("sourceTitle"):

            blogpost = Blogpost.objects.get(pk=Blogpost_id)
            source = Source()
            source.link = request.POST.get('sourceLink')
            source.title = request.POST.get('sourceTitle')
            source.blogpost = blogpost
            source.save()
                
        return HttpResponseRedirect(request.path_info)

    else:

        return render(request, "blog/sources.html", context)

@login_required
def edit(request, Blogpost_id):

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):

            blogpost=Blogpost.objects.get(pk=Blogpost_id)
            blogpost.title= request.POST.get('title')
            blogpost.subtitle= request.POST.get('subtitle')
            blogpost.author= request.POST.get('author')
            blogpost.content= request.POST.get('content')
            blogpost.img= request.POST.get('img')
            blogpost.save()

            messages.success(request, 'Post edited')
            return redirect('/')

    else :

        try:
            Blogpost.objects.get(pk=Blogpost_id)
        except Blogpost.DoesNotExist:
            raise Http404("This post does not exist")

        context ={
            "Blogpost" : Blogpost.objects.get(pk=Blogpost_id)
        }

        return render(request, "blog/edit.html", context)

@login_required
def logout(request):

    django_logout(request)

    return HttpResponseRedirect('/')

@login_required
def add(request):

    if request.method == "POST":

        if request.POST.get('title') and request.POST.get('content'):

            blogpost=Blogpost()
            blogpost.title= request.POST.get('title')
            blogpost.subtitle= request.POST.get('subtitle')
            blogpost.author= request.POST.get('author')
            blogpost.content= request.POST.get('content')
            blogpost.img= request.POST.get('img')
            blogpost.date_posted= datetime.datetime.now()
            blogpost.save()

            messages.success(request, 'Post added')


            return redirect('/')

    else :






        return render(request, "blog/add.html")

def contact(request):

    return render(request, "blog/contact.html")
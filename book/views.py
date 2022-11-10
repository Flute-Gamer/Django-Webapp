import io
from django.shortcuts import render
from django.http import FileResponse

from book.class_GeradorRelatorio import GeradorRelatorio
# Create your views here.

def login(request):
    return render(request, "login.html")

def inicial(request):
    return render(request, "inicial.html")

def cadastroVoos(request):
    return render(request, "cadastroVoos.html")

def relatorios(request):
    retornaRelatorioPDF(request)
    return render(request, "relatorios.html")

def monitoraVoos(request):
    return render(request, "monitoraVoos.html")


def retornaRelatorioPDF(request):
    buffer = io.BytesIO()
    buffer.seek(0)
    relatorio = GeradorRelatorio(None,None,None)
    relatorio.gera_pdf()
    return FileResponse(buffer, as_attachment=True, filename='requirements.txt')
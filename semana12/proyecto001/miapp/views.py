from django.shortcuts import render,HttpResponse,redirect,render

# Create your views here.

layout = """
    <h1> Proyecto Web (LP3) | Gomez Flores Elias </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio </a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de saludo </a>
        </li>
        <li>
            <a href="/rango"> Mostrar numeros [a,b] </a>
        </li>
    </ul>
    </hr>
"""





def index(request):

    return render(request, 'index.html')

def saludo(request):
    
    return render(request, 'saludo.html')

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Nuimeros de[{a},{b}] </h2>
        Resultado: <br>
        <ul>
"""
    while a<=b:
        resultado += f"<li>{a}</li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)

def rango2(request,a=0,b=100):
    resultado = f"""
        <h2> Nuimeros de[{a},{b}] </h2>
        Resultado: <br>
        <ul>
"""
    while a<=b:
        resultado += f"<li>{a}</li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)










from django.http.response import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import redirect,render
from django.urls import reverse
# Create your views here.
data={
    "telefon":"telefon kategorisindeki urunler",
    "bilgisayar":"bilgisayar kategorisindeki urunler",
    "elektronik":"elektronik kategorisindeki urunler"
}

def index(request):
    list_items=""
    category_list=list(data.keys())
    for category in category_list:
        redirect_path=reverse("products_by_category",args=[category])
        list_items += f"<li><a href =\"{redirect_path}\">{category}</a> </li>"

    html=f"<ul>{list_items}</ul>"
    return render(request,'myapp/index.html')


def getProductsByCategoryId(request,category_id):
    ids =list(data.keys())
    if category_id>len(ids):
        return HttpResponseNotFound("yanlis kategori secimi")

    category_name=ids[category_id-1]

    redirect_path=reverse("products_by_category",args=[category_name])

    return redirect(redirect_path)


def getProductsByCategory(request,category):
    try:
        category_text=data[category]
        return render(request,'myapp/products.html',{
            "category":category,
            "category_text":category_text
        })
    except:
        return HttpResponseNotFound(f"<h1>yanlis kategori secimi</h1>")



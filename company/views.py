from django.shortcuts import render
from django.views import View


class Company(View):
    def get(self, request):
        context = {
            'name': 'Company',
            'data': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Porro inventore totam vel, cumque iusto, saepe, quasi iste error odio nostrum vero nisi eaque aliquam qui fugiat! Minima, quo deleniti exercitationem inventore, illum nisi pariatur omnis nam maxime reprehenderit quibusdam soluta quaerat est alias consequatur temporibus tenetur quisquam facere consectetur vel excepturi ducimus, dicta iste? Aut ullam velit ipsam nihil sit earum praesentium? Distinctio molestiae minima laudantium voluptate mollitia similique, unde voluptatem a voluptatum qui iste aliquid quae perferendis eligendi magnam dolores, aspernatur delectus quidem adipisci ipsum quaerat. Voluptas, quasi, culpa, optio cumque placeat laboriosam explicabo inventore quia iure provident molestias!',
            'header': 'Company info',
        }

        return render(request, 'company.html', context=context)
    
class Contact(View):
    def get(self, request):
        context = {
            'name': 'Company',
            'data': '+38(066)6666666',
            'header': 'Number info',
        }
         
        return render(request, 'company.html', context=context)
    
class Map(View):
    def get(self, request):
        context = {
            'name': 'Company',
            'data': 'Contrada Lucia 996 Quarto Luce umbro, 38265 Padova (PA)',
            'header': 'Location info',
        }
        return render(request, 'company.html', context=context)
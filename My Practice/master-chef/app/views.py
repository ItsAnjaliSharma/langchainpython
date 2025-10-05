from django.shortcuts import render, redirect
from django.views import View
from app.forms import RecipeForm
from app.langchain import askChef
 
class Home(View):
    def get(self,request):
        form = RecipeForm()
        return render(request,'app/home.html', {'form':form})
    
    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data['recipe_message'] 
            ai_res_recipe= askChef(recipe_message)
            request.session['ai_recipe'] = ai_res_recipe
        form = RecipeForm()
        return redirect('/')

# class About(View):
#     def get(self,request):
#         return render(request,'about.html')

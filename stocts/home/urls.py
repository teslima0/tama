from django.urls import path
from .views import *
from .views import BlogHomeView, BlogArticleDetail,AddPostView,UpdatePostView, DeletePostForm, LikeView, AddCommentView, AddCategoryView, CategoryView, CategoryListView
#
urlpatterns = [
    path('', home, name = 'homepage'),
    path('about/', abouts, name = 'aboutpage'),
    path('cgpa/', other, name = 'otherpage'),
    path('cgp/', about, name = 'about'),
    path('resume/', resume, name = 'resume'),
    path('agecalculator', hom, name = 'homepag'),
    path('contact/', contacts, name = 'contactpage'),
    path('service/', services, name = 'servicepage'),
    path('portfolios/', portfolio, name = 'portfoliopage'),
    path('price/', pricing, name = 'pricepage'),
    path('portfolio-details/', portfolio_details, name = 'portfolio_detail_page'),
    path('team/', team, name = 'teampage'),
    path('testimomial/', testimonial, name = 'testimonialpage'),
    path('service/', service, name = 'service'),
    path('contact/', contact, name = 'contact'),
    path('add/', add, name = 'add'),
    path('cg/', cgp, name = 'cgpapage'),
    path('gpa/', gpa, name = 'gpa'),
    path('customer/', serve, name = 'serve'),

    path('blog/', BlogHomeView.as_view(), name = 'bloghomepage'),
    path('article/<int:pk>', BlogArticleDetail.as_view(), name = 'blogdetailpage'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/remove', DeletePostForm.as_view(), name = 'delete_post'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('category-list/', CategoryListView, name = 'category_list'),
    path('likes/<int:pk>', LikeView, name = 'like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name ='add_comment'),
]



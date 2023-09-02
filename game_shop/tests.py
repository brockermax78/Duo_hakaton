# from rest_framework.test import APITestCase,APIRequestFactory,force_authenticate
# from .models import Category,Games
# from django.contrib.auth import get_user_model
# from .views import GameViewSet
# from collections import OrderedDict

# User = get_user_model()

# class PostTest(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.category = Category.objects.create(title='cati')
#         user = User.objects.create_user(email='test@gmail.com',password='1234',name ='test',is_active=True)
#         self.token = '12345'

#         posts = [Games(author=user,body='test game 1',title='first  game',category=self.category,slug='1'),
#                  Games(author=user,body='test game 2',title='second game',category=self.category,slug='2'),
#                  Games(author=user,body='test game 3',title='third  game',category=self.category,slug='3')
#                 ]
#         Games.objects.bulk_create(posts)



#     def test_post_listing(self):
#         request = self.factory.get('api/v1/c-games/')
#         view = GameViewSet.as_view({'get':'list'})
#         response = view(request)
#         assert response.status_code == 200
#         assert type(response.data) == OrderedDict
        
#     def test_post_retrieve(self):
#         slug= Games.objects.all()[0].slug
#         request = self.factory.get(f'/rud-games/{slug}/')
#         view  = GameViewSet.as_view({'get':'retrieve'})
#         response = view(request, pk=slug)


#         assert response.status_code == 200

#     def test_post_create(self):
#         user = User.objects.all()[0]
#         data = {
#             'body': 'new_new',
#             'title': 'game4',
#             'category': 'cati',
#             'slug': 4
#         }
#         request = self.factory.post('/c-games/',data ,format='json')
#         force_authenticate(request,user,token=self.token)
#         view = GameViewSet.as_view({'c-games':'create'})
#         response = view(request)
#         assert response.data['author']==user.name

#     def test_post_update(self):
#         user = User.objects.all()[0]
#         data ={
#             'body': 'update advfv'
#         }
#         post = Games.objects.all()[2]
#         request = self.factory.patch(f'/c-games/{post.slug}', data, format='json')
#         force_authenticate(request, user, token=self.token)
#         view = GameViewSet.as_view({'patch': 'partial_update'})
#         response = view(request, pk=post.slug)
#         print(response.data)
#         assert Games.objects.get(slug=post.slug).body == data['body']

#     # def test_post_delete(self):
#     #     user = User.objects.all()[0]
#     #     post = Games.objects.all()[2]
#     #     request = self.factory.delete(f'/c-games/{post.slug}/')
#     #     force_authenticate(request,user)
#     #     view = GameViewSet.as_view({'delete':'destroy'})
#     #     response = view(request,pk=post.slug)

#     #     assert not Games.objects.filter(slug=post.slug).exists()
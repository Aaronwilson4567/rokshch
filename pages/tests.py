from django.test import SimpleTestCase
from django.urls import reverse
from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.



class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user= get_user_model().objects.create_user(username="testuser",email="test@email.com",password="test")
        cls.post=Post.objects.create(title="A good Title",body="Nice body content",author=cls.user)


    def test_post_model_(self):
        self.assertEqual(self.post.title,"A good Title")
        self.assertEqual(self.post.body,"Nice body content")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(str(self.post),"A good Title")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_post_createview(self):
        response=self.client.post(reverse("post_new"),{"title":"New title","body":"New text","author":self.user.id})
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,"New title")
        self.assertEqual(Post.objects.last().body,"New text")

    def test_post_updateview(self):
        response=self.client.post(reverse("post_edit",args="1"),{"title":"Updated title","body":"Updated text",},)
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,"Updated title")
        self.assertEqual(Post.objects.last().body,"Updated text")

    def test_post_deleteview(self):
        response=self.client.post(reverse("post_delete",args="1"))
        self.assertEqual(response.status_code,302)




        

        


# class HomepageTest(SimpleTestCase):
#     def test_url_exist_at_current_location(self):
#         response=self.client.get("/")
#         self.assertEqual(response.status_code,200)


#     def test_url_availabe_by_name(self):
#          response=self.client.get(reverse("home"))
#          self.assertEqual(response.status_code,200)

#     def test_template_name_correct(self):
#          response=self.client.get(reverse("home"))
#          self.assertTemplateUsed(response,"home.html")
    
#     def test_template_content(self):
#          response=self.client.get("home")
#          self.assertContains(response,"<h1> Hello django home page</h1>")



# class AboutpageTest(SimpleTestCase):
#     def test_url_exist_at_current_location(self):
#         response=self.client.get("/about/")
#         self.assertEqual(response.status_code,200)

#     def  test_url_available_by_name(self):
#         response=self.client.get(reverse("about"))
#         self.assertEqual(response.status_code,200)  

#     def test_template_name_correct(self):
#          response=self.client.get(reverse("about"))
#          self.assertTemplateUsed(response,"about.html") 


#     def test_template_content(self):
#          response=self.client.get("about")
#          self.assertContains(response,"<h1>about page</h1>")   
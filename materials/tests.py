from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from materials.models import Lesson, Course
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            id=1,
            username='admin',
            password=1234
        )

        self.lesson = Lesson.objects.create(
            id=3,
            title='test-урок',
            owner=self.user
        )

        self.course = Course.objects.create(
            id=2,
            title='test-курс',
            owner=self.user
        )

    def test_lesson_list(self):
        """тест на вывод листа с уроками"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/Lesson/list/'
        )
        print(f'ответ по тесту 1 - {response.json()}')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 3, 'title': 'test-урок', 'description': None, 'image': None, 'link': None, 'owner': 1}]}
        )

    def test_lesson_create(self):
        """тест на создание урока"""

        self.client.force_authenticate(user=self.user)

        data = {
            'id': 2,
            'title': 'test 2',
            'owner': self.user.id
        }

        response = self.client.post(
            '/Lesson/create/',
            data=data
        )

        print(f'ответ по тесту 2 - {response.json()}')

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )



    def test_lesson_update(self):
        """тест на редактирования урока"""

        self.client.force_authenticate(user=self.user)
        update_url = reverse('materials:Lesson-Update', args=[self.lesson.id])
        data = {
            'id': self.lesson.id,
            'title': 'update test 2',
        }

        response = self.client.patch(
            update_url,
            data=data,
        )

        print(f'ответ по тесту 3 - {response.json()}')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.data['title'],
            data['title']
        )




    def test_lesson_Retrieve(self):
        """тест на Retrieve урока"""

        self.client.force_authenticate(user=self.user)
        url = reverse('materials:Lesson-Retrieve', args=[self.lesson.id])
        data = {
            'id': self.lesson.id,
            'title': self.lesson.title,
        }

        response = self.client.get(
            url
        )

        print(f'ответ по тесту 4 - {response.json()}')

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.data['title'],
            data['title']
        )


    def test_lesson_Destroy(self):
        """тест на удаление урока"""


        self.client.force_authenticate(user=self.user)

        print(self.user.id)


        url = reverse('materials:Lesson-Destroy', args=[self.lesson.id])

        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.filter(id=self.lesson.id).exists()
        )


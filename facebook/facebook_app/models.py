from django.db import models
from datetime import date
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    #id
    username = models.CharField('User name',max_length=50)
    email = models.CharField('User email', max_length=50)
    password = models.CharField('User Password', max_length=20)

class Blog(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    title = models.CharField('Post title',max_length=100)
    description = models.TextField('Post Description')
    posted_date = models.DateField(default=date.today)
    good_name = models.CharField('Good name',max_length=100)

class Coment(models.Model):
    #id
    message = models.TextField('Message')
    date_comment = models.DateField(default=date.today)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

"""
class FriendList(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class FriendRequest(models.Model):
    request_from = models.IntegerField(default=0)
    request_to = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

#class FriendRequest(models.Model):
#    from_user = models.ForeignKey(User,related_name="from_user", on_delete=models.CASCADE)
#    to_user = models.ForeignKey(User,related_name="to_user", on_delete=models.CASCADE)
"""

class FriendList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, User):
        """
        add a new friend
        """
        if not User in self.friends.all():
            self.friend.add(User)
            #self.save()

    def remove_friend(self, User):
        """
        remove a friend
        """
        if User in self.friends.all():
            self.friends.remove(User)

    def unfriend(self, remove):
        """
        innitiate the action of unfriending someone
        """
        remover_friends_list = self # person terminating the friendship 
    
        # remove friend from remover friend list
        remover_friends_list.remove_friend(removee)

        #remove friend from removee friend list
        friends_list = FriendList.objects.get(user=removee)
        friend_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """
        is this a friend
        """
        if friend in self.friends.all():
            return True
        return False

class FriendRequest(models.Model):
    """
    a friend request consists of two main parts
    1 is sender:
        person sending/initiating the friend request
    2 is receiver:
        person receiving the friend request
    """

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=False, null=False, default=True)
    timestemp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """
        accept a friend request
        update both sender and reciver friend list
        """
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """
        decline a friend request
        it is declined by setting the is_active field to false
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
        cancle a friend request
        it is cancelled by settings the is_active field to false
        this is only different with respect to declining through the notification that
        is generated.
        """
        self.is_active = False
        self.save()
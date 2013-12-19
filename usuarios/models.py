# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group


class UsuarioManager(BaseUserManager):
    
    def _create_user(self, dni, password, is_admin, is_superuser):
        if not dni:
            raise ValueError('El dni debe ingresarse')
        user = self.model(dni=dni, is_active=True, is_admin=is_admin, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, dni, password=None):
        return self._create_user(dni, password, False, False)

    def create_superuser(self, dni, password):
        return self._create_user(dni, password, True, True)

    def create_userRol(self, dni, tipo, password):
        if tipo == Usuario.ESTUDIANTE:
            user = self.model(dni=dni, tipo=tipo, is_active=True, is_admin=False, is_superuser=False)
        if tipo == Usuario.DIRECTOR:         
            try:
                user = Usuario.objects.get(dni=dni)
            except Usuario.DoesNotExist:
                user = None
            if user is not None:
                grupo = Group.objects.get(name=tipo)
                user.groups.add(grupo)
                return user
            user = self.model(dni=dni, tipo=tipo, is_active=True, is_admin=True, is_superuser=False)           
        if tipo == Usuario.COORDINADOR:
            user = self.model(dni=dni, tipo=tipo, is_active=True, is_admin=True, is_superuser=False)
        if tipo == Usuario.JURADO:
            user = self.model(dni=dni, tipo=tipo, is_active=True, is_admin=False, is_superuser=False)
        if tipo == Usuario.ASESOR:
            try:
                user = Usuario.objects.get(dni=dni)
            except Usuario.DoesNotExist:
                user = None
            if user is not None:
                grupo = Group.objects.get(name=tipo)
                user.groups.add(grupo)
                return user
            user = self.model(dni=dni, tipo=tipo, is_active=True, is_admin=False, is_superuser=False)
       
        user.set_password(password)
        user.save(using=self._db)

        # aqui agrego el grupo de permiso
        grupo = Group.objects.get(name=user.tipo)
        user.groups.add(grupo)

        return user

def TIPO_USERS_FROM_GROUP():
    lista = Group.objects.only("name")
    TIPO = {}
    for name in lista:
        TIPO[str(name.name)] = str(name.name)
    return TIPO.iteritems()



class Usuario(AbstractBaseUser, PermissionsMixin):

    ESTUDIANTE   = 'estudiante'
    DIRECTOR     = 'director'
    COORDINADOR  = 'coordinador'
    ASESOR       = 'asesor'
    JURADO       = 'jurado'
    
    TIPO_USUARIO = (
        (ESTUDIANTE, 'Estudiante'),
        (DIRECTOR, 'Director'),
        (COORDINADOR, 'Coordinador T.Grado'),
        (ASESOR, 'Asesor'),
        (JURADO, 'Jurado'),
    )

    dni       = models.IntegerField(unique=True)
    tipo      = models.CharField(max_length=50, choices=TIPO_USUARIO) 

    is_active = models.BooleanField(default=True)
    is_admin  = models.BooleanField(default=False)

    objects   = UsuarioManager()
    
    USERNAME_FIELD = 'dni'
    #REQUIRED_FIELDS = ['']

    def get_full_name(self):
        return "%s" % self.dni

    def get_short_name(self):
        return "%s" % self.dni

    def get_absolute_url(self):
        return '/usuario/' #reverse('main.views.persona', args=[str(self.id)])

    def __unicode__(self):
        return "%s" % self.dni

    @property
    def is_staff(self):
        return self.is_admin
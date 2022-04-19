from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, correo,nombre,rol, password):
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        
        correo=self.normalize_email(correo)
        nuevoUsuario = self.model(correo=correo, nombre=nombre,rol=rol,password=password)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save(using=self._db)
        return nuevoUsuario

    def create_superuser(self, correo,nombre,rol,password):
        usuario = self.create_user(correo,nombre,rol,password)
        usuario.is_superuser= True
        usuario.is_staff=True
        usuario.save(using=self._db)
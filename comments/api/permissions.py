from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        
        else:
            id_comment = view.kwargs['pk']                  # De la vista sacamos el id del comentario
            comment = Comment.objects.get(pk=id_comment)    # Obtenemos el comentario con es id
            id_user = request.user.pk                       # Obtenemos el id del usuario que hace la petición  
            id_user_comment = comment.user_id               # Obtenemos el id del usuario que hizo el comentario
            if id_user == id_user_comment:                  # Comparamos si el usuario que hace la petición es el mismo que hizo el comentario
                return True
            return False                                    # Si no es el mismo usuario, no tiene permiso para hacer la petición
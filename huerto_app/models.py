from django.db import models

# ----------------------------
# Modelo de Usuario
# ----------------------------
class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_usuario')
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre


# ----------------------------
# Modelo de Planta
# ----------------------------
class Planta(models.Model):
    planta_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    planta_nom = models.CharField(max_length=100)
    tipo_planta = models.CharField(max_length=50, blank=True)
    cuidados = models.TextField(blank=True)
    foto_url = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'planta'

    def __str__(self):
        return f"{self.planta_nom} ({self.usuario.nombre})"


# ----------------------------
# Cuidados Programados
# ----------------------------
class CuidadoProgramado(models.Model):
    id = models.AutoField(primary_key=True)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    tipo_cuidado = models.CharField(max_length=20)
    frecuen_dias = models.IntegerField()
    prox_fecha = models.DateField()
    detalles = models.TextField(blank=True)

    class Meta:
        db_table = 'cuidado_programado'

    def __str__(self):
        return f"{self.tipo_cuidado} - {self.planta.planta_nom}"


# ----------------------------
# Historial de acciones
# ----------------------------
class HistorialAccion(models.Model):
    id = models.AutoField(primary_key=True)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    accion = models.CharField(max_length=20)
    comentario = models.TextField(blank=True)
    fecha_accion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historial'

    def __str__(self):
        return f"{self.accion} - {self.planta.planta_nom} ({self.fecha_accion.date()})"


# ----------------------------
# Notificaciones
# ----------------------------
class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    planta = models.ForeignKey('Planta', on_delete=models.CASCADE)
    tipo_noti = models.CharField(max_length=20)
    fecha_envio = models.DateTimeField()
    enviado = models.BooleanField(default=False)
    mensaje = models.TextField(blank=True)

    class Meta:
        db_table = 'notificacion'

    def __str__(self):
        return f"{self.tipo_noti} - {self.planta.planta_nom} - {'✅' if self.enviado else '⏳'}"

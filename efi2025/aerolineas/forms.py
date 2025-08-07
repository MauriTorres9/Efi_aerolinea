from django import forms
from .models import Vuelo, Reserva, Pasajero, Boleto, Usuario, Avion, Asiento
from django.core.exceptions import ValidationError

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ["avion", "origen", "destino", "fecha_salida", "fecha_llegada", "duracion"]
        widgets = {
            'avion': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
            'origen': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Ciudad de origen'
            }),
            'destino': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Ciudad de destino'
            }),
            'fecha_salida': forms.DateTimeInput(attrs={
                'class': 'form-control  personalizado',
                'type': 'datetime-local'
            }),
            'fecha_llegada': forms.DateTimeInput(attrs={
                'class': 'form-control  personalizado',
                'type': 'datetime-local'
            }),
            'duracion': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'HH:MM:SS'
            }),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["vuelo", "pasajero", "asiento", "estado", "fecha_reserva", "precio"]
        widgets = {
            'vuelo': forms.Select(attrs={
                'class': 'form-control personalizado'
            }),
            'pasajero': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
            'asiento': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
            'fecha_reserva': forms.DateTimeInput(attrs={
                'class': 'form-control  personalizado',
                'type': 'datetime-local'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control personalizado',
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        vuelo = cleaned_data.get("vuelo")
        pasajero = cleaned_data.get("pasajero")
        asiento = cleaned_data.get("asiento")
        
        if vuelo and asiento:
            avion = vuelo.avion
            if asiento not in avion.asiento_set.all():
                raise ValidationError("El asiento seleccionado no pertenece al avión asignado a este vuelo.")
            
        if vuelo and pasajero:
            if Reserva.objects.filter(vuelo=vuelo, pasajero=pasajero).exists():
                raise ValidationError("Este pasajero ya tiene una reserva para este vuelo.")
            
        if asiento and asiento.estado != 'Disponible':
            raise ValidationError("El asiento seleccionado no está disponible.")

        return cleaned_data

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = ["nombre", "documento", "email", "telefono", "fecha_nacimiento", "tipo_documento"]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Nombre completo'
            }),
            'documento': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Número de documento'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Correo electrónico'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Teléfono'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control  personalizado',
                'type': 'date'
            }),
            'tipo_documento': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
        }

class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ["reserva", "codigo_barra", "fecha_emision", "estado"]
        widgets = {
            'reserva': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
            'codigo_barra': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Código de barras'
            }),
            'fecha_emision': forms.DateTimeInput(attrs={
                'class': 'form-control personalizado',
                'type': 'datetime-local'
            }),
             'estado': forms.Select(attrs={
                'class': 'form-control personalizado'
            }),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "password", "email", "rol"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electronico'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ["modelo", "capacidad", "filas", "columnas"]
        widgets = {
            'modelo': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Modelo del avión'
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Capacidad total'
            }),
            'filas': forms.NumberInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Cantidad de filas'
            }),
            'columnas': forms.NumberInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Cantidad de columnas'
            }),
        }

class AsientoForm(forms.ModelForm):
    class Meta:
        model = Asiento
        fields = ["numero", "fila", "columna", "tipo", "estado"]
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Número de asiento'
            }),
            'fila': forms.NumberInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Fila'
            }),
            'columna': forms.NumberInput(attrs={
                'class': 'form-control  personalizado',
                'placeholder': 'Columna'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control  personalizado'
            }),
        }

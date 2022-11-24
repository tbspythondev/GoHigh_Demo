from django import forms

class UpdateProfile(forms.Form):
    name = forms.CharField(label='name', max_length=100)

    def __init__(self, *args, **kw):
        super(UpdateProfile, self).__init__()
        self.fields['name']="xyz"
        # print(self.instance.name,"self.instance.name")

        # self.fields['name'].initial = self.instance.name
    class Meta:
       fields = "name"
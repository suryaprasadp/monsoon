from django import forms


# form which is displayed for queries: Contains Query for variable and Year. Also the file upload from which queries are to be made.
class initial_page(forms.Form):
    var=forms.CharField(required=True, label="Query Variable", help_text="Please enter the query variable")
    year=forms.IntegerField(required=True, label="Query Year", help_text="Please enter the relevant year")
    docfile=forms.FileField( required=True, label='Upload file')
     
    
    def clean_renewal_date(self):
        data = self.cleaned_data['var','year','docfile']
        return data
    
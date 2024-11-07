from django.shortcuts import render
from .forms import DocumentForm
from .utils import extract_text
from .ipa_conversion import replace_abbreviations_with_ipa

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            original_text = extract_text(doc.uploaded_file.path)
            processed_text = replace_abbreviations_with_ipa(original_text)
            return render(request, 'doc_app/display.html', {
                'original_text': original_text,
                'processed_text': processed_text,
                'filename': doc.uploaded_file.name
            })
    else:
        form = DocumentForm()
    return render(request, 'doc_app/upload.html', {'form': form})

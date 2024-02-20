from django.shortcuts import render
from django.http import HttpResponse

ProgrammingLanguagesArray = [
    {
        'name': 'C#',
        'image': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230305130205/Csharp1.png',
        'desc': 'C# is a general-purpose high-level programming language supporting multiple paradigms. C# encompasses static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented, and component-oriented programming disciplines.'
    },
    {
        'name': 'Python',
        'image': 'https://www.ntuclearninghub.com/documents/39367/4216797/Python-Symbol.png/369e410e-a90f-f887-c2dc-61f7ef761476/',
        'desc': 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming.',
    },
    {
        'name': 'JavaScript',
        'image': 'https://www.orientsoftware.com/Themes/OrientSoftwareTheme/Content/Images/blog/2021-12-16/what-can-you-do-with-javascript-thumb.jpg',
        'desc': 'JavaScript, often abbreviated as JS, is a programming language and core technology of the World Wide Web, alongside HTML and CSS. As of 2024, 98.9% of websites use JavaScript on the client side for webpage behavior, often incorporating third-party libraries.',
    },
    {
        'name': 'TypeScript',
        'image': 'https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2018/08/typescriptfeature.png',
        'desc': 'TypeScript is a free and open-source high-level programming language developed by Microsoft that adds static typing with optional type annotations to JavaScript. It is designed for the development of large applications and transpiles to JavaScript',
    },
    {
        'name': 'Java',
        'image': 'https://1000logos.net/wp-content/uploads/2020/09/Java-Logo.png',
        'desc': 'Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.',
    },
    {
        'name': 'Dart',
        'image': 'https://miro.medium.com/v2/resize:fit:1400/1*QCajckOeBhRaLzi0RoFqig.png',
        'desc': 'Dart is a programming language designed by Lars Bak and Kasper Lund and developed by Google. It can be used to develop web and mobile apps as well as server and desktop applications. Dart is an object-oriented, class-based, garbage-collected language with C-style syntax.',
    }
]

# Create your views here.
def ProgrammingLanguages(request):
    return render(request, 'ProgrammingLanguages.html', { 'ProgrammingLanguagesArray': ProgrammingLanguagesArray })
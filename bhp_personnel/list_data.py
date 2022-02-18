from edc_list_data import PreloadData


list_data = {
    'bhp_personnel.studies': [
        ('potlako', 'Potlako'),
        ('ambition', 'Ambition'),
        ('cancer', 'Cancer'),
        ('flourish', 'Flourish'),
    ],
    'bhp_personnel.skills': [
        ('teamwork', 'Teamwork'),
        ('communication', 'Communication'),
        ('problem_solving', 'Problem Solving'),
    ]
}

preload_data = PreloadData(
    list_data=list_data)

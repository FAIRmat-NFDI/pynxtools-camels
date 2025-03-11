try:
    from nomad.config.models.plugins import (
        AppEntryPoint,
        # ExampleUploadEntryPoint,
        # ParserEntryPoint,
        # SchemaPackageEntryPoint,
    )
except ImportError as exc:
    raise ImportError(
        "Could not import nomad package. Please install the package 'nomad-lab'."
    ) from exc

from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemHistogram,
    MenuItemOption,
    MenuItemPeriodicTable,
    MenuItemTerms,
    MenuSizeEnum,
    SearchQuantities,
)

schema = 'pynxtools.nomad.schema.Root'

app_entry_point = AppEntryPoint(
    name='Automation App',
    description='Simple Generic NeXus app.',
    app=App(
        # Label of the App
        label='Automation CAMELS',
        # Path used in the URL, must be unique
        path='automation',
        # Used to categorize apps in the explore menu
        category='Experiment',
        # Brief description used in the app menu
        description='A simple search app customized for generic NeXus data.',
        # Longer description that can also use markdown
        readme='This page allows to search for generic NeXus Experiment Entries. It is similar to the entries search, but with reduced filter set, modified menu on the left and different shown columns. The dashboard directly shows useful interactive statistics about the data',
        # # Label of the App
        # label="Simple Scan",
        # # Path used in the URL, must be unique
        # path="nxsensor_scan",
        # # Used to categorize apps in the explore menu
        # category="Experiment",
        # # Brief description used in the app menu
        # description="Search simple scan experiments (NXsensor_scan and inheriting classes), including output of NOMAD CAMELS",
        # # Longer description that can also use markdown
        # readme="This page allows to search for generic experimental entries corresponding to NXsensor_scan and inheriting from it classes, including output of NOMAD CAMELS. It is similar to the entries search, but with reduced filter set, modified menu on the left and different shown columns. The dashboard directly shows useful interactive statistics about the data",
        # If you want to use quantities from a custom schema, you need to load
        # the search quantities from it first here. Note that you can use a glob
        # syntax to load the entire package, or just a single schema from a
        # package.
        search_quantities=SearchQuantities(
            include=[f'*#{schema}'],
        ),
        # Controls which columns are shown in the results table
        columns=[
            Column(title='Entry ID', search_quantity='entry_id', selected=True),
            Column(
                title='File Name',
                search_quantity='mainfile',
                selected=True,
            ),
            Column(
                title='Start Time',
                # search_quantity=f"min_by(data.ENTRY, &start_time#{schema}).start_time#{schema}",
                search_quantity=f'data.ENTRY[*].start_time#{schema}',
                selected=True,
            ),
            Column(
                title='Description',
                search_quantity=f'data.ENTRY[*].experiment_description__field#{schema}',
                selected=True,
            ),
            Column(
                title='Author',
                search_quantity=f'[data.ENTRY[*].USER[*].name__field, data.ENTRY[*].userID[*].name__field]#{schema}',
                selected=True,
            ),
            Column(
                title='Sample',
                search_quantity=f'data.ENTRY[*].SAMPLE[*].name__field#{schema}',
                selected=True,
            ),
            Column(
                title='Sample ID',
                search_quantity=f'data.ENTRY[*].SAMPLE[*].sample_id__field#{schema}',
                selected=False,
            ),
            Column(
                title='Definition',
                search_quantity=f'data.ENTRY[*].definition__field#{schema}',
                selected=True,
            ),
            # Column(
            #     title="Protocol",
            #     search_quantity=f"data.ENTRY[*].NOTE[?name=='protocol'].file_name__field#{schema}#str",
            #     selected=False,
            # ),
        ],
        # Dictionary of search filters that are always enabled for queries made
        # within this app. This is especially important to narrow down the
        # results to the wanted subset.
        # filters_locked={
        #     f'data.ENTRY.definition__field#{schema}': 'NXsensor_scan',
        # },
        filters_locked={'section_defs.definition_qualified_name': [schema]},
        # Controls the menu shown on the left
        menu=Menu(
            size=MenuSizeEnum.MD,
            title='Menu',
            items=[
                Menu(
                    title='Elements',
                    size=MenuSizeEnum.XXL,
                    items=[
                        MenuItemPeriodicTable(
                            search_quantity='results.material.elements',
                        ),
                        MenuItemTerms(
                            search_quantity='results.material.chemical_formula_hill',
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            search_quantity='results.material.chemical_formula_iupac',
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            search_quantity='results.material.chemical_formula_reduced',
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            search_quantity='results.material.chemical_formula_anonymous',
                            width=6,
                            options=0,
                        ),
                        MenuItemHistogram(
                            x='results.material.n_elements',
                        ),
                    ],
                ),
                Menu(
                    title='Experiment type',
                    size=MenuSizeEnum.LG,
                    items=[
                        MenuItemTerms(
                            title='Entry Type',
                            search_quantity='entry_type',
                            width=12,
                            options=12,
                        ),
                        MenuItemTerms(
                            title='NeXus Class',
                            search_quantity=f'data.ENTRY.definition__field#{schema}',
                            width=12,
                            options=12,
                        ),
                    ],
                ),
                Menu(
                    title='Instruments',
                    size=MenuSizeEnum.LG,
                    items=[
                        MenuItemTerms(
                            title='Model',
                            search_quantity=f'data.ENTRY.INSTRUMENT.name__field#{schema}',
                            width=12,
                            options=12,
                        ),
                        MenuItemTerms(
                            name='Name',
                            search_quantity=f'data.ENTRY.INSTRUMENT.name#{schema}',
                            width=12,
                            options=12,
                        ),
                    ],
                ),
                Menu(
                    title='Samples',
                    size=MenuSizeEnum.LG,
                    items=[
                        MenuItemTerms(
                            title='Name',
                            search_quantity=f'data.ENTRY.SAMPLE.name__field#{schema}',
                            width=12,
                            options=12,
                        ),
                        MenuItemTerms(
                            title='Sample ID',
                            search_quantity=f'data.ENTRY.SAMPLE.sample_id__field#{schema}',
                            width=12,
                            options=12,
                        ),
                    ],
                ),
                Menu(
                    title='Authors / Origin',
                    size=MenuSizeEnum.LG,
                    items=[
                        MenuItemTerms(
                            title='Entry Author',
                            search_quantity=f'data.ENTRY.USER.name__field#{schema}',
                            width=12,
                            options=5,
                        ),
                        MenuItemTerms(
                            title='User ID / Entry Author',
                            search_quantity=f'data.ENTRY.userID.name__field#{schema}#str',
                            width=12,
                            options=5,
                        ),
                        MenuItemTerms(
                            title='Upload Author',
                            search_quantity='authors.name',
                            width=12,
                            options=5,
                        ),
                        MenuItemTerms(
                            title='Affiliation',
                            search_quantity=f'data.ENTRY.USER.affiliation__field#{schema}',
                            width=12,
                            options=5,
                        ),
                    ],
                ),
                MenuItemHistogram(
                    title='Start Time',
                    x=f'data.ENTRY.start_time#{schema}',
                    autorange=True,
                ),
                MenuItemHistogram(
                    title='Upload Creation Time',
                    x='upload_create_time',
                    autorange=True,
                ),
                Menu(
                    title='Protocols (NOMAD CAMELS)',
                    size=MenuSizeEnum.LG,
                    items=[
                        MenuItemTerms(
                            title='CAMELS files',
                            search_quantity=f'data.ENTRY.PROCESS.program__field#{schema}',
                            width=12,
                            options={
                                'NOMAD CAMELS': MenuItemOption(
                                    label='NOMAD CAMELS entries only',
                                ),
                            },
                            show_header=False,
                            show_input=False,
                        ),
                        MenuItemTerms(
                            title='Protocols (only for CAMELS files)',
                            search_quantity=f'data.ENTRY.NOTE.file_name__field#{schema}#str',
                            width=12,
                            options=12,
                        ),
                    ],
                ),
            ],
        ),
        # Controls the default dashboard shown in the search interface
        dashboard={
            'widgets': [
                {
                    'type': 'periodic_table',
                    'scale': 'linear',
                    'quantity': 'results.material.elements',
                    'layout': {
                        'lg': {'minH': 3, 'minW': 3, 'h': 7, 'w': 10, 'y': 0, 'x': 0}
                    },
                },
                # {
                #     "type": "histogram",
                #     "show_input": False,
                #     "autorange": True,
                #     "nbins": 30,
                #     "scale": "linear",
                #     "quantity": f"data.ENTRY.start_time#{schema}",
                #     "title": "Start Time",
                #     "layout": {
                #         "lg": {"minH": 3, "minW": 3, "h": 7, "w": 10, "y": 7, "x": 0}
                #     },
                # },
                {
                    'type': 'terms',
                    'show_input': True,
                    'scale': 'linear',
                    'quantity': 'entry_type',
                    'title': 'Entry Type',
                    'layout': {
                        'lg': {'minH': 3, 'minW': 3, 'h': 7, 'w': 4, 'y': 0, 'x': 10}
                    },
                },
                {
                    'type': 'terms',
                    'show_input': True,
                    'scale': 'linear',
                    'quantity': f'data.ENTRY.definition__field#{schema}',
                    'title': 'NeXus Class',
                    'layout': {
                        'lg': {'minH': 3, 'minW': 3, 'h': 7, 'w': 4, 'y': 0, 'x': 14}
                    },
                },
                {
                    'type': 'terms',
                    'show_input': True,
                    'scale': 'linear',
                    'quantity': f'data.ENTRY.USER.name__field#{schema}',
                    'title': 'Author',
                    'layout': {
                        'lg': {'minH': 3, 'minW': 3, 'h': 7, 'w': 4, 'y': 0, 'x': 18}
                    },
                },
                {
                    'type': 'terms',
                    'show_input': True,
                    'scale': 'linear',
                    'quantity': f'data.ENTRY.SAMPLE.name__field#{schema}',
                    'title': 'Sample',
                    'layout': {
                        'lg': {'minH': 3, 'minW': 3, 'h': 7, 'w': 4, 'y': 0, 'x': 22}
                    },
                },
            ]
        },
    ),
)


#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

pyfgt_antivirus
==========

1) Import the Task you like::

    from nornir_pyfgt.plugins.tasks import pyfgt_antivirus


2) Use in a script::

    from nornir_pyfgt.plugins.tasks import pyfgt_antivirus
    from nornir_utils.plugins.functions import print_result
    from nornir import InitNornir

    nr = InitNornir(config_file="your/config")

    results = nr.run(task=pyfgt_antivirus)

    print_result(results)

Output::
    [ { 'analytics-accept-filetype': 0,
    'analytics-db': 'disable',
    'analytics-ignore-filetype': 0,
    'av-block-log': 'enable',
    'av-virus-log': 'enable',
    'cifs': { 'archive-block': '',
              'archive-log': '',
              'av-scan': 'disable',
              'emulator': 'enable',
              'external-blocklist': 'disable',
              'fortindr': 'disable',
              'fortisandbox': 'disable',
              'outbreak-prevention': 'disable',
              'quarantine': 'disable'},
    'comment': 'Scan files and block viruses.',
    'content-disarm': { 'cover-page': 'enable',
                        'detect-only': 'disable',
                        'error-action': 'log-only',
                        'office-action': 'enable',
                        'office-dde': 'enable',
                        'office-embed': 'enable',
                        'office-hylink': 'enable',
                        'office-linked': 'enable',
                        'office-macro': 'enable',
                        'original-file-destination': 'discard',
                        'pdf-act-form': 'enable',
                        'pdf-act-gotor': 'enable',
                        'pdf-act-java': 'enable',
                        'pdf-act-launch': 'enable',
                        'pdf-act-movie': 'enable',
                        'pdf-act-sound': 'enable',
                        'pdf-embedfile': 'enable',
                        'pdf-hyperlink': 'enable',
                        'pdf-javacode': 'enable'},
    'ems-threat-feed': 'disable',
    ...
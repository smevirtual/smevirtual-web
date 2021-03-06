#!/usr/bin/env python
# Copyright (C) SME Virtual Network contributors. All rights reserved.
# See LICENSE in the project root for license information.

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError("Could not import Django.")
        raise

    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, 'smevirtual'))

    execute_from_command_line(sys.argv)

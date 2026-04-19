# Source Generated with Decompyle++
# File: project.pyc (Python 3.12)

from __future__ import annotations
import sys
import os
from pathlib import Path
from argparse import ArgumentParser, RawTextHelpFormatter
from project_lib import QmlProjectData, check_qml_decorators, is_python_file, migrate_pyproject, QMLDIR_FILE, MOD_CMD, METATYPES_JSON_SUFFIX, SHADER_SUFFIXES, TRANSLATION_SUFFIX, requires_rebuild, run_command, remove_path, ProjectData, resolve_valid_project_file, new_project, NewProjectTypes, ClOptions, DesignStudioProject
DESCRIPTION = '\npyside6-project is a command line tool for creating, building and deploying Qt for Python\napplications. It operates on project files which are also used by Qt Creator.\n\nOfficial documentation:\nhttps://doc.qt.io/qtforpython-6/tools/pyside-project.html\n'
OPERATION_HELP = {
    'build': 'Build the project. Compiles resources, UI files, and QML files if existing and necessary.',
    'run': 'Build and run the project.',
    'clean': 'Clean build artifacts and generated files from the project directory.',
    'qmllint': 'Run the qmllint tool on QML files in the project.',
    'deploy': 'Create a deployable package of the application including all dependencies.',
    'lupdate': 'Update translation files (.ts) with new strings from source files.',
    'migrate-pyproject': 'Migrate a *.pyproject file to pyproject.toml format.' }
UIC_CMD = 'pyside6-uic'
RCC_CMD = 'pyside6-rcc'
LRELEASE_CMD = 'pyside6-lrelease'
LUPDATE_CMD = 'pyside6-lupdate'
QMLTYPEREGISTRAR_CMD = 'pyside6-qmltyperegistrar'
QMLLINT_CMD = 'pyside6-qmllint'
QSB_CMD = 'pyside6-qsb'
DEPLOY_CMD = 'pyside6-deploy'

def _sort_sources(files = None):
    '''Sort the sources for building, ensure .qrc is last since it might depend
       on generated files.'''
    
    def key_func(p = None):
        if p.suffix != '.qrc':
            return p.suffix

    return sorted(files, key = key_func)


class Project:
    '''
    Class to wrap the various operations on Project
    '''
    
    def __init__(self = None, project_file = None):
        self.project = ProjectData(project_file = project_file)
        self.cl_options = ClOptions()
        self._qml_module_sources = []
        self._qml_module_dir = None
        self._qml_dir_file = None
        self._qml_project_data = QmlProjectData()
        self._qml_module_check()

    
    def _qml_module_check(self):
        '''Run a pre-check on Python source files and find the ones with QML
        decorators (representing a QML module).'''
        if not self.cl_options.qml_module and self.project.qml_files:
            return None
        for file in self.project.files:
            if not is_python_file(file):
                continue
            (has_class, data) = check_qml_decorators(file)
            if not has_class:
                continue
            self._qml_module_sources.append(file)
            if not data:
                continue
            self._qml_project_data = data
        if not self._qml_module_sources:
            return None
        if not self._qml_project_data:
            print('Detected QML-decorated files, but was unable to detect QML_IMPORT_NAME')
            sys.exit(1)
        self._qml_module_dir = self.project.project_file.parent
        for uri_dir in self._qml_project_data.import_name.split('.'):
            pass
        print(self._qml_module_dir)
        self._qml_module_dir / QMLDIR_FILE = None
        if not self.cl_options.quiet:
            count = len(self._qml_module_sources)
            print(f'''{self.project.project_file.name}, {count} QML file(s), {self._qml_project_data}''')
            return None

    
    def _get_artifacts(self = None, file = None, output_path = None):
        """Return path and command for a file's artifact"""
        if file.suffix == '.ui':
            py_file = f'''{file.parent}/ui_{file.stem}.py'''
            return ([
                Path(py_file)], [
                UIC_CMD,
                os.fspath(file),
                '--rc-prefix',
                '-o',
                py_file])
        if None.suffix == '.qrc':
            if not output_path:
                py_file = f'''{file.parent}/rc_{file.stem}.py'''
            else:
                py_file = str(output_path.resolve())
            return ([
                Path(py_file)], [
                RCC_CMD,
                os.fspath(file),
                '-o',
                py_file])
    # WARNING: Decompyle incomplete

    
    def _regenerate_qmldir(self):
        """Regenerate the 'qmldir' file."""
        if not self.cl_options.dry_run or self._qml_dir_file:
            return None
        if self.cl_options.force or requires_rebuild(self._qml_module_sources, self._qml_dir_file):
            qf = self._qml_dir_file.open('w')
            qf.write(f'''module {self._qml_project_data.import_name}\n''')
            for f in self._qml_module_dir.glob('*.qmltypes'):
                qf.write(f'''typeinfo {f.name}\n''')
            None(None, None)
            return None
        return None
        with None:
            if not None:
                pass

    
    def _build_file(self = None, source = None, output_path = None):
        '''Build an artifact if necessary.'''
        (artifacts, command) = self._get_artifacts(source, output_path)
        for artifact in artifacts:
            if self.cl_options.force or requires_rebuild([
                source], artifact):
                run_command(command, cwd = self.project.project_file.parent)
            self._build_file(artifact)

    
    def build_design_studio_resources(self):
        '''
        The resources that need to be compiled are defined in autogen/settings.py
        '''
        ds_project = DesignStudioProject(self.project.main_file)
        resources_file_path = ds_project.get_resource_file_path()
    # WARNING: Decompyle incomplete

    
    def build(self):
        '''Build the whole project'''
        for sub_project_file in self.project.sub_projects_files:
            Project(project_file = sub_project_file).build()
        if self._qml_module_dir:
            self._qml_module_dir.mkdir(exist_ok = True, parents = True)
        for file in _sort_sources(self.project.files):
            self._build_file(file)
        if DesignStudioProject.is_ds_project(self.project.main_file):
            self.build_design_studio_resources()
        self._regenerate_qmldir()

    
    def run(self = None):
        '''Runs the project'''
        self.build()
        cmd = [
            sys.executable,
            str(self.project.main_file)]
        return run_command(cmd, cwd = self.project.project_file.parent)

    
    def _clean_file(self = None, source = None):
        '''Clean an artifact.'''
        (artifacts, command) = self._get_artifacts(source)
        for artifact in artifacts:
            remove_path(artifact)
            self._clean_file(artifact)

    
    def clean(self):
        '''Clean build artifacts.'''
        for sub_project_file in self.project.sub_projects_files:
            Project(project_file = sub_project_file).clean()
        for file in self.project.files:
            self._clean_file(file)
        if self._qml_module_dir and self._qml_module_dir.is_dir():
            remove_path(self._qml_module_dir)
            if self._qml_module_dir.parent != self.project.project_file.parent:
                project_dir_parts = len(self.project.project_file.parent.parts)
                first_module_dir = self._qml_module_dir.parts[project_dir_parts]
                remove_path(self.project.project_file.parent / first_module_dir)
        if DesignStudioProject.is_ds_project(self.project.main_file):
            DesignStudioProject(self.project.main_file).clean()
            return None

    
    def _qmllint(self):
        '''Helper for running qmllint on .qml files (non-recursive).'''
        if not self.project.qml_files:
            print(f'''{self.project.project_file.name}: No QML files found''', file = sys.stderr)
            return None
        cmd = [
            QMLLINT_CMD]
        if self._qml_dir_file:
            cmd.extend([
                '-i',
                os.fspath(self._qml_dir_file)])
        for f in self.project.qml_files:
            cmd.append(os.fspath(f))
        run_command(cmd, cwd = self.project.project_file.parent, ignore_fail = True)

    
    def qmllint(self):
        '''Run qmllint on .qml files.'''
        self.build()
        for sub_project_file in self.project.sub_projects_files:
            Project(project_file = sub_project_file)._qmllint()
        self._qmllint()

    
    def deploy(self):
        '''Deploys the application'''
        cmd = [
            DEPLOY_CMD]
        cmd.extend([
            str(self.project.main_file),
            '-f'])
        run_command(cmd, cwd = self.project.project_file.parent)

    
    def lupdate(self):
        for sub_project_file in self.project.sub_projects_files:
            Project(project_file = sub_project_file).lupdate()
        if not self.project.ts_files:
            print(f'''{self.project.project_file.name}: No .ts file found.''', file = sys.stderr)
            return None
        source_files = self.project.python_files + self.project.ui_files
        project_dir = self.project.project_file.parent
    # WARNING: Decompyle incomplete



def main(mode, dry_run, quiet, force = None, qml_module = None, project_dir = None, project_path = (None, False, False, False, None, None, None, False), legacy_pyproject = ('mode', 'str', 'dry_run', 'bool', 'quiet', 'bool', 'force', 'bool', 'qml_module', 'bool', 'project_dir', 'str', 'project_path', 'str', 'legacy_pyproject', 'bool')):
    cl_options = ClOptions(dry_run = dry_run, quiet = quiet, force = force, qml_module = qml_module)
    new_project_type = NewProjectTypes.find_by_command(mode)
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    parser = ArgumentParser(description = DESCRIPTION, formatter_class = RawTextHelpFormatter)
    parser.add_argument('--quiet', '-q', action = 'store_true', help = 'Quiet')
    parser.add_argument('--dry-run', '-n', action = 'store_true', help = 'Only print commands')
    parser.add_argument('--force', '-f', action = 'store_true', help = 'Force rebuild')
    parser.add_argument('--qml-module', '-Q', action = 'store_true', help = 'Perform check for QML module')
    subparsers = parser.add_subparsers(dest = 'mode', required = True)
    for project_type in NewProjectTypes:
        new_parser = subparsers.add_parser(project_type.value.command, help = project_type.value.description)
        new_parser.add_argument('project_dir', help = 'Name or location of the new project', nargs = '?', type = str)
        new_parser.add_argument('--legacy-pyproject', action = 'store_true', help = 'Create a legacy *.pyproject file')
    for op_mode, op_help in OPERATION_HELP.items():
        op_parser = subparsers.add_parser(op_mode, help = op_help)
        op_parser.add_argument('project_path', nargs = '?', type = str, help = 'Path to the project file')
    args = parser.parse_args()
    main(args.mode, args.dry_run, args.quiet, args.force, args.qml_module, getattr(args, 'project_dir', None), getattr(args, 'project_path', None), getattr(args, 'legacy_pyproject', None))
    return None

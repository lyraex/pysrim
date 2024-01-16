""" Write Inputfile for SRIM and TRIM calculations

"""


class AutoTRIM(object):
    def __init__(self, mode=1, restart_directroy=None):
        """Writes a file AUTOTRIM to TRIM directory for autostart

        Parameters
        ----------
        mode : int
            (0) TRIM runs normally, (1) TRIM runs without keyboard input,
            (2) TRIM resumes running its last saved calculation. Default 1
            and is really the only sane option when using Python for automation
        restart_directory : str
            currently not implemented. default None
        """
        self._mode = mode

    def write(self):
        """ write AUTOTRIM in current directory """
        with open('TRIMAUTO', 'w') as f:
            f.write('{}'.format(self._mode))


class TRIMInput(object):
    """Input File representation of TRIM run

    Parameters
    ----------
    trim : :class:`srim.srim.TRIM`
        A TRIM calculation to use for writing a file
    """
    newline = '\r\n' # TRIM uses microsoft newlines

    def __init__(self, trim):
        self._trim = trim

    @property
    def srim_num_elements(self):
        """Number of unique elements in target (layer elements treated as unique)"""
        return sum(len(layer.elements) for layer in self._trim.target.layers)

    def _write_title(self):
        return (
            'This file controls TRIM Calculations '
            'generated by pysrim'
        ) + self.newline

    def _write_ion(self):
        return (
            'Ion: Z, Mass [amu], Energy [keV], Angle [degrees], '
            'Number Ions, Bragg Corr, AutoSave Number'
        ) + self.newline + '{} {} {} {} {} {} {}'.format(
            self._trim.ion.atomic_number,
            self._trim.ion.mass,
            self._trim.ion.energy / 1000.0, # eV -> keV
            self._trim.settings.angle_ions,
            self._trim.number_ions,
            self._trim.settings.bragg_correction,
            self._trim.settings.autosave
        ) + self.newline

    def _write_cascade_options(self):
        return (
            'Cascades(1=Kitchn-Peese, 2=Full-Cascade, 3=Sputtering, '
            '4-5=Ions;6-7=Neutrons), Random Number Seed, Reminders'
        ) + self.newline + '{} {} {}'.format(
        self._trim.calculation,
            self._trim.settings.random_seed,
            self._trim.settings.reminders
        ) + self.newline

    def _write_plot_on_off(self):
        return (
            'Diskfiles (0=no,1=yes): RANGES.txt, BACKSCATT.txt, '
            'TRANSMIT.txt, Sputtered, COLLISIONS.txt(0=no, 1=Ion, '
            '2=Ion+Recoils), Special EXYZ.txt file'
        ) + self.newline + '{} {} {} {} {} {}'.format(
            self._trim.settings.ranges,
            self._trim.settings.backscattered,
            self._trim.settings.transmit,
            self._trim.settings.sputtered,
            self._trim.settings.collisions,
            self._trim.settings.exyz
        ) + self.newline

    def _write_target(self):
        return (
            'Target material : Number of Elements, Number of Layers'
        ) + self.newline + '"{}" {} {}'.format(
            self._trim.settings.description,
            self.srim_num_elements,
            len(self._trim.target.layers),
        ) + self.newline

    def _write_plot_options(self):
        return (
            'PlotType (0-5); Plot Depths: Xmin, Xmax(Ang.) '
            '[=0 0 for Viewing Full Target]'
        ) + self.newline + '{} {} {}'.format(
            self._trim.settings.plot_mode,
            self._trim.settings.plot_xmin,
            self._trim.settings.plot_xmax
        ) + self.newline

    def _write_elements(self):
        elements_str = (
            'Target Elements:    Z   Mass [amu]'
        ) + self.newline
        index = 1
        for layer in self._trim.target.layers:
            for element in layer.elements:
                elements_str += 'Atom {} = {} =     {} {}'.format(
                    index,
                    element.symbol,
                    element.atomic_number,
                    element.mass
                ) + self.newline
                index += 1
        return elements_str

    def _write_layer(self):
        layers_str_header_1 = 'Layer    Layer Name   Width Density'
        layers_str_header_2 = 'Number   Description  (Ang) (g/cm^3)'
        layers_str = []

        for layer in self._trim.target.layers:
            for element in layer.elements:
                layers_str_header_1 += '  {}({})'.format(element.symbol, element.atomic_number)
                layers_str_header_2 += 'Stoich'

        element_index = 0
        for layer_index, layer in enumerate(self._trim.target.layers, start=1):
            layer_str = '{} "{}" {} {}'.format(layer_index, layer.name, layer.width, layer.density)
            layer_str += ' 0.0' * element_index
            for element in layer.elements:
                layer_str += ' {} '.format(layer.elements[element]['stoich'])
            layer_str += ' 0.0' * (self.srim_num_elements - element_index - len(layer.elements))
            element_index += len(layer.elements)
            layers_str.append(layer_str)
        return self.newline.join([layers_str_header_1, layers_str_header_2] + layers_str) + self.newline

    def _write_solid_gas(self):
        return (
            '0  Target layer phases (0=Solid, 1=Gas)'
        ) + self.newline + ' '.join(str(layer.phase) for layer in self._trim.target.layers) + self.newline

    def _write_bragg_correction(self):
        return (
            'Target Compound Corrections (Bragg)'
        ) + self.newline + ' ' + ' '.join([str(layer.bragg_correction) for layer in self._trim.target.layers]) + self.newline

    def _write_displacement_energies(self):
        ed_str = (
            'Individual target atom displacement energies (eV)'
        ) + self.newline

        for layer in self._trim.target.layers:
            for element in layer.elements:
                ed_str += ' {}'.format(layer.elements[element]['E_d'])
        return ed_str + self.newline

    def _write_lattice_binding(self):
        lattice_str = (
            'Individual target atom lattice binding energies (eV)'
        ) + self.newline

        for layer in self._trim.target.layers:
            for element in layer.elements:
                lattice_str += ' {}'.format(layer.elements[element]['lattice'])
        return lattice_str + self.newline

    def _write_surface_binding(self):
        surface_str = (
            'Individual target atom surface binding energies (eV)'
        ) + self.newline

        for layer in self._trim.target.layers:
            for element in layer.elements:
                surface_str += ' {}'.format(layer.elements[element]['surface'])
        return surface_str + self.newline

    def _write_version(self):
        return (
            'Stopping Power Version (1=2011, 0=2011)'
        ) + self.newline + '{}'.format(self._trim.settings.version) + self.newline

    def write(self):
        """Write TRIMInput class to ``TRIM.IN``"""
        with open('TRIM.IN', 'wb') as f:
            methods = [
                self._write_title,
                self._write_ion,
                self._write_cascade_options,
                self._write_plot_on_off,
                self._write_target,
                self._write_plot_options,
                self._write_elements,
                self._write_layer,
                self._write_solid_gas,
                self._write_bragg_correction,
                self._write_displacement_energies,
                self._write_lattice_binding,
                self._write_surface_binding,
                self._write_version
            ]

            input_str = ''
            for method in methods:
                input_str += method.__call__()

            f.write(input_str.encode('utf-8'))


class SRInput(object):
    """Input file for Stopping and Range (Calculations)

    Parameters
    ----------
    sr : :class:`srim.srim.SR`
        SR class to use for writting file
    """
    newline = '\r\n' # TRIM uses microsoft newlines

    def __init__(self, sr):
        self._sr = sr

    def _write_filename(self):
        return (
            '---Stopping/Range Input Data (Number-format: Period = Decimal Point)'
        ) + self.newline + (
            '---Output File Name'
        ) + self.newline + '{}'.format(
            self._sr.settings.output_filename
        ) + self.newline

    def _write_ion(self):
        return (
            '---Ion(Z), Ion Mass(u)'
        ) + self.newline + '{} {}'.format(
            self._sr.ion.atomic_number,
            self._sr.ion.mass
        ) + self.newline

    def _write_layer_info(self):
        return (
            '---Target Data: (Solid=0,Gas=1), Density(g/cm3), Compound Corr.'
        ) + self.newline + '{} {} {}'.format(
            self._sr.layer.phase,
            self._sr.layer.density,
            self._sr.settings.correction
        ) + self.newline + (
            '---Number of Target Elements'
        ) + self.newline + '{}'.format(
            len(self._sr.layer.elements)
        ) + self.newline

    def _write_elements(self):
        elements_str = (
            '---Target Elements: (Z), Target name, Stoich, Target Mass(u)'
        ) + self.newline

        for element in self._sr.layer.elements:
            elements_str += '{} "{}" {} {}'.format(
                element.atomic_number,
                element.name,
                self._sr.layer.elements[element]['stoich'],
                element.mass
            ) + self.newline
        return elements_str

    def _write_output_options(self):
        return (
            '---Output Stopping Units (1-8)'
        ) + self.newline + '{}'.format(
            self._sr.settings.output_type
        ) + self.newline

    def _write_ion_energy_range(self):
        return (
            '---Ion Energy : E-Min(keV), E-Max(keV)'
        ) + self.newline + '{} {}'.format(
            self._sr.settings.energy_min / 1.0e3,
            self._sr.ion.energy / 1.0e3
        ) + self.newline

    def write(self):
        """Write SR calcualtion to ``SR.IN``"""
        with open('SR.IN', 'wb') as f:
            methods = [
                self._write_filename,
                self._write_ion,
                self._write_layer_info,
                self._write_elements,
                self._write_output_options,
                self._write_ion_energy_range
            ]

            input_str = ''
            for method in methods:
                input_str += method.__call__()

            f.write(input_str.encode('utf-8'))

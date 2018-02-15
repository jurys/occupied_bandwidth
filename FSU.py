import visa
import time
import numpy as np

class FSU(object):

    #esu = 0

    def __init__(self, adr: object) -> object:
        self.adr = adr

    def open_over_gpib(self):
        rm = visa.ResourceManager()
        self.esu = rm.open_resource(self.adr)
        print(self.esu.query('*IDN?'))

    def set_start_stop_f(self,f_start, f_stop):
        """Set start and stop frequency



                    Args:
                        f_start (int): start frequency in Hz
                        f_stop (int): stop frequency in Hz
                    Returns:


                    Raises:
                        IOError: Start Frequency is smaller then Stop Frequency
                    """

        if (f_stop < f_start):
            print('Start Frequency is smaller then Stop Frequency')
        else:
            self.esu.write('FREQ:START ' + str(f_start) + 'Hz')
            self.esu.write('FREQ:STOP ' + str(f_stop) + 'Hz')

    def info(self):
        return self.esu.query('*IDN?')

    def preset(self):
        self.esu.write("*rst")

    def get_y_trace(self, trace_nr):
        return self.esu.query("TRAC? trace" + str(trace_nr))

    def get_trace_data(self, trace_nr):
        """Querry the trace data

            This command queries the previously captured trace data for the specified trace from
            the memory. As an offset and number of sweep points to be retrieved can be specified,
            the trace data can be retrieved in smaller portions, making the command faster than
            the TRAC:DATA? command. This is useful if only specific parts of the trace data are of
            interest.

            Args:
                trace_nr (int): Trace 1-6

            Returns:
                ASCII Format (FORMat ASCII):
                The data is stored as a list of comma-separated values (CSV) of the measured values
                in floating point format.

            Raises:
                IOError: data not ready
            """


        while True:
            try:
                #status = self.esu.query("STATus:OPERation:EVENt?")
                #print(bin(status))
                y_trace = self.esu.query("TRAC? trace"+str(trace_nr))
                points = self.esu.query('SWE:POIN?')
                f_start = self.esu.query("FREQ:START?")
                f_stop = self.esu.query("FREQ:STOP?")

                break
            except:
                print('data not ready')
        step = (int(f_stop) - int(f_start)) / int(points)
        x_trace = np.arange(int(f_start), int(f_stop), step)
        trace = ''
        for x in x_trace:
            trace = trace +','+ str(x)
        #x_trace = ','.join(x_trace)
        trace = trace[1:]

        x_trace = trace
        return x_trace, y_trace

    def set_RBW(self,rbw):
        self.esu.write('BAND ' + str(rbw) + 'Hz')

    def set_VBW(self, vbw):
        self.esu.write('BAND ' + str(vbw) + 'Hz')

    def set_RBW_xVBW(self, rbw , x=3 ): #rbw (int) in Hz
        self.esu.write('BAND '+str(rbw)+'Hz')
        self.esu.write('BAND:VID '+str(x*rbw)+'Hz')

    def start(self):
        self.esu.write("INIT;*WAI")
        #self.esu.write('*ESE 1')
        #time.sleep(5)
        #a = self.esu.query('STATus:OPERation:EVENt?')
        #print(bin(int(a)))

    def send_SCPI(self, command):
        self.esu.write(command)

    def set_span(self, span):
        self.esu.write('FREQ:SPAN '+str(span)+'Hz')

    def set_center(self, center):
        self.esu.write('FREQ:CENT ' + str(center)+'Hz')

    def set_sweep_auto_on_off(self, state):
        if(state==1 or state=='on'or state=="ON"):
            self.esu.write('SWE:TIME:AUTO ON')
        else:
            self.esu.write('SWE:TIME:AUTO OFF')

    def set_sweep_time_10_x_auto(self):
        self.set_sweep_auto_on_off(1)
        time_sweep = self.esu.query('SWE:TIME?')
        #print(time_sweep)
        self.set_sweep_auto_on_off(0)
        time_sweep = float(time_sweep)*50
        #print(time_sweep)
        self.esu.write('SWE:TIME '+ str(time_sweep) +'s')

    def set_sweep_time(self, time):
        self.esu.write('SWE:TIME ' + str(time) + 's')

    def set_detector(self, detector, trace_nr=1):
        self.esu.write('SENS:DET' + str(trace_nr) + ' ' + detector)

    def set_continuous_mode_on_off(self, state):
        if (state==1 or state=='on'or state=="ON"):
            self.esu.write('INIT:CONT ON')
        else:
            self.esu.write('INIT:CONT OFF')

    def choose_transducer(self, name):
        self.esu.write('CORR:TRAN:SEL '+"'"+name+"'")
        self.esu.write('CORR:TRAN ON')

    def set_sweep_points(self, points):
        if(points in range(101, 100001)):
            self.esu.write('SWE:POIN '+str(points))
        else:
            print('Sweep points out of range :' + str(points))
            #self.esu.write('SWE:TIME:AUTO ON')
            self.esu.write('SWE:POIN 101')

    def set_sweep_counter(self, counter):
        self.esu.write('SWE:COUNT '+str(counter))

    def sent_SCPI(self, command):
        self.esu.write(command)

    def get_marker(self):
        marker_y = self.esu.query('CALC:MARK1:Y?')
        marker_x = self.esu.query('CALC:MARK1:X?')
        return marker_x, marker_y

    def query(self, command):
        return self.esu.query(str(command))

def main():
    esu = FSU('GPIB0::2::INSTR')

    esu.open_over_gpib()
    esu.preset()
    esu.send_SCPI('INST:SEL SAN')
    esu.set_continuous_mode_on_off(0)

    esu.set_RBW_3VBW(10000)
    esu.set_span(1000000)


    esu.set_sweep_time_10_x_auto()
    esu.set_sweep_counter(2)
    #time.sleep(5)

    esu.start()
    #time.sleep(5)
    x,y = esu.get_trace_data(1)
    print(y)
    print(x)

if __name__ == '__main__':
    main()
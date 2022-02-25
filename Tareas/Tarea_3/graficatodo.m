function InfoRet = graficatodo(InputSet, OutFile)
%   InfoRet = polinomio (INPUTSET, OUTFILE) crea salida HTML
%   y archivo de imagen OUTFILE.  Retorna una salida HTML en InfoRet.

%   Entradas : campos tipo char de la pagina polinomio.html
%      Inputset.fun: fucion de x
%      Inputset.min: Limite minimo de valores del eje x
%      Inputset.max: Limite maximo de valores del eje x
%
%   Entradas : campos tipo char dados por matweb
%      Inputset.mldir  : directorio de trabajo 
%      Inputset.mlid   : identificador unico para esta llamada
% 
%   Usa un archivo polinomio_g.html para desplegar la grafica
%   Genera un archivo "wsrml#####.jpeg"
%------------------------------------------------------------

% Se pasan los valores del archivo html a esta aplicacion y se le asignan
% variables. Min y max se convierten de string a double.
fun = InputSet.fun;
min = str2double(InputSet.min);
max = str2double(InputSet.max);

% Ajuste de ubicacion (path) de almacenamiento de los archivos.
cd(InputSet.mldir);

% Elimina los .jpeg de mas de una hora de existencia.
wscleanup('wsrml*.jpeg', 1);

%Crea una matriz x, donde min es el primer valor, max es el ultimo valor y
%en las demas posiciones aumenta el valor en incrementos de 0.1
x=min:0.01:max;

%Crea una matriz y de acuerdo a la expresion siguiente. Son los valores y
%del polinomio.
y=eval(fun);

% Plotea la grafica
Fig = figure('visible','off');
plot(x,y), grid on;
ylabel('Eje y');
xlabel('Eje x');
title(['Funcion']);

% Ajuste del tamaño
pos = get(gcf, 'position'); %"get" retorna las propiedades del objeto
                            %"gcf" get current figure handle
pos(3) = 400; % ancho
pos(4) = 400; % altura
set(gcf, 'Position', pos, 'PaperPosition', [.25 .25 4 4]); % ajusta las propiedades del objeto

% Crea el archivo jpeg
PlotFile = sprintf('wsr%s.jpeg', InputSet.mlid);

% Actualiza imagen
drawnow; 
wsprintjpeg(Fig, PlotFile);
close(Fig);

templatefile = which('graficatodog.html');
if ( exist('OutFile','var') == 1 )
  s.GraphFileName = [ PlotFile];
  InfoRet = htmlrep(s, templatefile, OutFile);
else
  s.GraphFileName = ['/icons/' PlotFile];
  InfoRet = htmlrep(s, templatefile);
end

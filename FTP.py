import os
from os.path import exists
from getpass import getpass
from ftplib import FTP
import ftplib


class ProtractorFTP:
    def _init_(self, file, site_ip, dir, user=()):
        self.__file = file
        self.__site_ip = site_ip 
        self.__dir = dir
        self.__user = user
    
    #verifica se o arquivo existe, se for o caso
    #e se nãoestivermos no modo refech devemos sair da função
    # verbose indica qual operaçoes estão sendo realizadas
    #refecth caso exista um arquivo REDME no pc se deve ou não baixa-lo
    def downloadfile(self,verbose=True, refeth=False):
        if exists(self.__file) and not refeth:
            if verbose:
                return 0
        #abre o local do arquivo
        local = open(self.__file, 'wb')
        try:         
            remote = FTP(self.__site_ip) # cria a conexao com o serv
            remote.login(*self.__user)# realiza o login
            remote.cwd(self.__dir) # muda o diretorio
            remote.retrbinary('RETR ' + self.__file, local.write, 1024)  # baixa o rquivo  no  modo  binario
            remote.quit() # fecha a coneção
        finally:
            local.close() #fecha o arquivo
            
    def uploadfile(self, verbose=True):
        if verbose:
            return 0
        try:
            local = open(self.__file, 'rb') #abre o local do arquivo a ser enviado
            remote = ftplib.FTP(self.__site_ip) # cria a conexao com o serv
            remote.login(*self.__user)# realiza o login
            remote.cwd(self.__dir) # muda o diretorio
            remote.retrbinary('STOR ' + self.__file, local, 1024)  # baixa o rquivo  no  modo  binario
            
        finally:
            remote.quit() # fecha a coneção
            local.close()#fecha o arquivo
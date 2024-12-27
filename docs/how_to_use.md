
## How to use this module

Before using this module, you need to register your application in the Google Cloud portal. To do this, you must follow these steps:

1. Go to [Google Console](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard) to create a new project (If you already have one created, skip this step) and fill in the data indicated in the form

![](imgs/proyectonuevo.png)

In the top bar you will see the name of the project. If it is not displayed, switch to the created project by clicking on the in the menu that is highlighted in the image.

![](imgs/seleccionarproyecto.png)

2. Go to **API and Services** on the left panel, and after changing to the page, click on **ENABLE APIs AND SERVICES**

![](imgs/habilitarapiyservicios.png)

3. Within the "Search API and services" search engine, type **Google Drive API**. Then, enable the API by clicking on **Enable**

![](imgs/gdriveApi.png)

You will be redirected to the API configuration page.

4. In the side panel, click on **OAuth consent screen**. If you have a corporate Gmail account, you will be able to use the API indefinitely and you will see that the user type is **Internal**. If you have a free Gmail account, you will have to give consent once a week to be able to connect to your email account. Your user type is **External** and you will have to add test users. Then press the **Create** button

![](imgs/pantallaDeCons.png)

5. Select the name of the app and the required fields as appropriate. Then click next.

![](imgs/infoApp.png)

6. Skip the **Permissions** screen, click the Save and Continue button at the bottom of the page.

![](imgs/permisos.png)

7. On the **Test Users** screen, click the **Add User** button and add your user. Click Save and Continue

![](imgs/usuarioprueba.png)

8. Go from the Left Navigation Menu to **Credentials**. Press **+Create Credentials** and indicate the option **OAuth Client ID**

![](imgs/crearcredencialesok.png)

9. Select as Application Type: **Desktop App**. Enter a name for the application and press the **Create** button

![](imgs/appEscritorio.png)

10. It will create the credentials for us. If we want to log in with the json file, we click on **Download JSON** and then on **Accept**. It is important to keep the downloaded file. It will be used later in the module. If we want to log in with the credentials, we save the Client ID and the Secret ID to use them later in the module.

![](imgs/credencialesDescarga.png)

Note: When the first connection is made, a .pickle file will be created in the Rocketbot root folder, to connect to the same service from another account you must delete
that file. Do the same procedure for the case in which the credentials expire.

---

## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. Para esto, debes seguir los siguientes pasos:

1. Ir a [Consola de Google](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard) para crear un nuevo proyecto (Si ya tienes uno creado, omita este paso) y complete los datos indicados en el formulario

![](imgs/proyectonuevo.png)

En la barra superior verás el nombre del proyecto. Si no se visualiza, cambie al proyecto creado haciendo click en la en el menu que se encuentra remarcado en la imagen.

![](imgs/seleccionarproyecto.png)

2. Ve a **API y Servicios** del panel izquierdo, y luego de cambiar a la página, hacer click en **HABILITAR APIs Y SERVICIOS**

![](imgs/habilitarapiyservicios.png)

3. Dentro del buscador "Buscar API y servicios" escriba **Google Drive API**. Luego, habilitar la API dando click en **Habilitar**

![](imgs/gdriveApi.png)

Se redireccionará a la página de configuración de la API.

4. En el panel lateral haga click en **Pantalla de consentimiento de OAuth**, si tienes una cuenta corporativa de gmail, podrás utilizar la API indefinidamente y verás que el tipo de usuario es **Interno**. Si cuentas con una cuenta gmail gratuita, tendrás que dar el consentimiento una vez a la semana para poder conectarte a tu cuenta de correo, tu tipo de usuario es **Externo** y deberás agregar usuarios de prueba. Luego presiona el botón **Crear**

![](imgs/pantallaDeCons.png)

5. Seleccionar el nombre de la app y los campos obligatorios según cada caso. A continuación haga click en siguiente.

![](imgs/infoApp.png)


6. Saltearse la pantalla de **Permisos**, haga click en el botón Guardar y Continuar que se encuentra a final de página.

![](imgs/permisos.png)

7. En la pantalla de **Usuarios de prueba** haga click en el botón **Add User** y agregue su usuario. Haga click en Guardar y Continuar

![](imgs/usuarioprueba.png)

8. Dirigirse desde el Menu de Navegación Izquierdo a **Credenciales**. Presione **+Crear Credenciales** e indique la opción **ID de cliente de OAuth**

![](imgs/crearcredencialesok.png)

9. Seleccionar como Tipo de Aplicación: **App de Escritorio**. Coloca un nombre para la aplicación y presione el botón **Crear**

![](imgs/appEscritorio.png)

10. Nos creará las credenciales, si queremos loguearnos con el archivo json damos click en **Descargar JSON** y luego en **Aceptar**. Es importante mantener el archivo descargado. Se utilizará más adelante en el módulo. Si queremos loguearnos con las credenciales, guardamos el Client ID y el Secret ID para usarlo más adelante el módulo.

![](imgs/credencialesDescarga.png)


Nota: Cuando se realice la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio desde otra cuenta, debe eliminar
ese archivo Realice el mismo procedimiento para el caso en que caduquen las credenciales.

---

## Como usar este módulo

Antes de utilizar este módulo, é necessário cadastrar sua aplicação no portal Google Cloud. Para isso, você deve seguir os seguintes passos:

1. Acesse o [Google Console](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard) para criar um novo projeto (se você já tiver um criado, pule esta etapa) e conclua o dados indicados no formulário

![](imgs/proyectonuevo.png)

Na barra superior você verá o nome do projeto. Caso não seja exibido, mude para o projeto criado clicando no menu destacado na imagem.

![](imgs/seleccionarproyecto.png)

2. Vá para **API e Serviços** no painel esquerdo e após mudar para a página, clique em **ATIVAR APIS E SERVIÇOS**

![](imgs/habilitarapiyservicios.png)

3. No mecanismo de pesquisa "Pesquisar APIs e serviços", digite **Google Drive API**. Em seguida, habilite a API clicando em **Ativar**

![](imgs/gdriveApi.png)

Você será redirecionado para a página de configuração da API.

4. No painel lateral clique em **Tela de consentimento do OAuth**, se você tiver uma conta corporativa do Gmail, poderá usar a API indefinidamente e verá que o tipo de usuário é **Interno**. Se você tiver uma conta gratuita do Gmail, terá que dar consentimento uma vez por semana para poder se conectar à sua conta de e-mail. Seu tipo de usuário é **Externo** e você terá que adicionar usuários de teste. Em seguida, pressione o botão **Criar**

![](imgs/pantallaDeCons.png)

5. Selecione o nome do aplicativo e os campos obrigatórios de acordo com cada caso. Em seguida, clique em próximo.

![](imgs/infoApp.png)


6. Ignore a tela **Permissões** e clique no botão Salvar e Continuar na parte inferior da página.

![](imgs/permisos.png)


7. Na tela **Usuários de teste** clique no botão **Adicionar usuário** e adicione seu usuário. Clique em Salvar e continuar

![](imgs/usuarioprueba.png)

8. Vá do menu de navegação à esquerda para **Credenciais**. Pressione **+Criar credenciais** e insira a opção **ID do cliente OAuth**

![](imgs/crearcredencialesok.png)

9. Selecione o tipo de aplicativo: **Aplicativo de desktop**. Insira um nome para o aplicativo e pressione o botão **Criar**

![](imgs/appEscritorio.png)

10. Irá criar as credenciais, se quisermos fazer o login com o arquivo json clicamos em **Baixar JSON** e depois em **Aceitar**. É importante manter o arquivo baixado. Ele será usado posteriormente no módulo. Se quisermos fazer login com as credenciais, salvamos o Client ID e o Secret ID para usar posteriormente no módulo.

![](imgs/credencialesDescarga.png)

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para conectar ao mesmo serviço de outra conta, você precisa deletar
esse arquivo Faça o mesmo procedimento caso as credenciais expirem.
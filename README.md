ADDI Challenge

### Analisis

1. Las personas de ventas hacen uso del CRM interno de la empresa para validar si realmente un lead puede convertirse en prospecto de la empresa en base a la infomacion suministrada por este, las personas de ventas validan esta informacion de forma manual verificando sus datos.

2. Por lo anterior se requiere hacer algo mas automatizado dentro del CRM donde permita a las personas de ventas poder saber si un cliente si puede ser prospecto o no de la empresa, de una manera mas eficiente.

3. Hay que tener encuenta que para validar los datos de las personas el CRM debe hacer uso de dos sistemas externos con el fin de validar esta informacion.

4. El CRM ya posee la informacion general de todos los clientes potenciales dentro del CRM
    * número de identificación nacional
    * fecha de nacimiento
    * nombre
    * apellido
    * correo electrónico

5. Hay varias validaciones que se realizan para verificar si realmente este cliente potencial si puede ser prospecto o no de la empresa estas son:
    * El cliente potencial debe existir en el sistema un externo de datos, toda la informacion que se encuentra dentro del CRM debe conincidir con la del sistema externo
    * El cliente potencial no debe poseer antecedentes judiciales en otro sistema externo
    * El CRM da una calificacion a estos prospecto entre 0 y 100, si el puntaje del prospecto es mayor de 60 este puede ser prospecto

6. Las dos primera validaciones deben correrse en paralelo, si las dos pasan estos datos se envian al sistema de calificacion para puntear el prospecto en base a dicha informacion

### Mejoras

1. Todos los datos de los prospectos deben coincidir con los datos del sistema externo de identificación del registro nacional?, ya que puede que algunos datos no sean tan relevantes como el caso del correo electrónico de la persona, ya que esta puede tener un correo electronico diferente registrado en dicho sistema externo o inclusive puede que en este sistema la persona no poseea esta informacion.

2. Que criterios usa el sistema de calificacion para puntear un prospecto entre 0 y 100, segun los datos obtenidos del sistema externo. en el proyecto se realizo de forma aleatoria, pero deberia realizarse un calculo mas racional.

3. Se podria gregar la informacion de fecha y expedicion de documento de identificación, con el fin de tener mas certeza que el lead es quien dice ser.
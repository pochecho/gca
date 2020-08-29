using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Contactos2.Models
{
    public class Contactos
    {
        [Key]
        public String Id { get; set; }
        public String Foto { get; set; }
        public String Nombre { get; set; }
        public String Apellido { get; set; }
        public String Telefono { get; set; }
        public String Correo { get; set; }

        public Contactos()
        {
            this.Id = Guid.NewGuid().ToString();
        }
    }
}

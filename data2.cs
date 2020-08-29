using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace Contactos2.Models
{
    public class ContactoXGrupo
    {
        public int Id { get; set; }
        public String Id_Contacto { get; set; }
        [ForeignKey("Id_Contacto")]
        public virtual Contactos FK_Contactos { get; set; }
        public int Id_Grupo { get; set; }
        [ForeignKey("Id_Grupo")]
        public virtual Grupos FK_Grupo { get; set; }
    }
}

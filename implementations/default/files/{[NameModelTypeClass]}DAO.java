package {[CompanyName]}.infrastructure.repository.{[NameModelLowerCamelCase]};

import jakarta.persistence.*;
import java.io.Serializable;
import java.sql.Time;
import java.util.Collection;
import java.util.Date;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@Table(name = "{[Table]}")
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class {[NameModelTypeClass]}DAO {
  {[PersistencePropertyDefinitions]}


}

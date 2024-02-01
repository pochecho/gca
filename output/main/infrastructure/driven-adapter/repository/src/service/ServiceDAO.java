package fare.infrastructure.repository.service;

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
@Table(name = "services")
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class ServiceDAO {
  
	@Id
	@Column(name = "id")
	public String id;
  
	@Column(name = "client_id")
	public String clientId;
  
	@Column(name = "employee_ids")
	public List<String> employeeIds;
  
	@Column(name = "date")
	public Date date;
  
	@Column(name = "inner_observations")
	public String innerObservations;
  
	@Column(name = "employee_observations")
	public String employeeObservations;
  
	@Column(name = "cost")
	public float cost;
  
	@Column(name = "status")
	public String status;
  
	@Column(name = "financial_status")
	public String financialStatus;
  
	@Column(name = "initial_hour")
	public float initialHour;
  
	@Column(name = "final_hour")
	public float finalHour;


}

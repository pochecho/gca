package fare.domain.entities.service;


public class ServiceEntity {
  
  	public String id;
  	public String clientId;
  	public List<String> employeeIds;
  	public Date date;
  	public String innerObservations;
  	public String employeeObservations;
  	public float cost;
  	public String status;
  	public String financialStatus;
  	public float initialHour;
  	public float finalHour;

  public ServiceEntity(
	String id, 
	String clientId, 
	List<String> employeeIds, 
	Date date, 
	String innerObservations, 
	String employeeObservations, 
	float cost, 
	String status, 
	String financialStatus, 
	float initialHour, 
	float finalHour
  ){
	this.id = id; 
	this.clientId = clientId; 
	this.employeeIds = employeeIds; 
	this.date = date; 
	this.innerObservations = innerObservations; 
	this.employeeObservations = employeeObservations; 
	this.cost = cost; 
	this.status = status; 
	this.financialStatus = financialStatus; 
	this.initialHour = initialHour; 
	this.finalHour = finalHour;
  }

  public ServiceEntity(){}


	public String getId(){
		return id;
	}

	public void setId(String id){
		this.id = id;
	}


	public String getClientId(){
		return clientId;
	}

	public void setClientId(String clientId){
		this.clientId = clientId;
	}


	public List<String> getEmployeeIds(){
		return employeeIds;
	}

	public void setEmployeeIds(List<String> employeeIds){
		this.employeeIds = employeeIds;
	}


	public Date getDate(){
		return date;
	}

	public void setDate(Date date){
		this.date = date;
	}


	public String getInnerObservations(){
		return innerObservations;
	}

	public void setInnerObservations(String innerObservations){
		this.innerObservations = innerObservations;
	}


	public String getEmployeeObservations(){
		return employeeObservations;
	}

	public void setEmployeeObservations(String employeeObservations){
		this.employeeObservations = employeeObservations;
	}


	public float getCost(){
		return cost;
	}

	public void setCost(float cost){
		this.cost = cost;
	}


	public String getStatus(){
		return status;
	}

	public void setStatus(String status){
		this.status = status;
	}


	public String getFinancialStatus(){
		return financialStatus;
	}

	public void setFinancialStatus(String financialStatus){
		this.financialStatus = financialStatus;
	}


	public float getInitialHour(){
		return initialHour;
	}

	public void setInitialHour(float initialHour){
		this.initialHour = initialHour;
	}


	public float getFinalHour(){
		return finalHour;
	}

	public void setFinalHour(float finalHour){
		this.finalHour = finalHour;
	}



  
}

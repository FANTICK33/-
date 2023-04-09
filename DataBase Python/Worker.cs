class Worker
{
  public int id;
  public string dep_id;
  public int age;
  public string full_name;
  public int salary;

  public Worker(int id, string dep_id, int age, string full_name, int salary)
  {
    this.id = id;
    this.dep_id = dep_id;
    this.age = age;
    this.full_name = full_name;
    this.salary = salary;
  }

  public override string ToString()
  {
    return $"id: {self.id}  Full name: {self.full_name}  age: {self.age}  salary: {self.salary}  dep id: {self.dep_id}";
  }


}
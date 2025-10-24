import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ConvertToUppercaseFunctionTest{
	@Test
	public void  testThatConvertInputToUppercase(){
	
		ConvertToUppercase convertToUppercase = new ConvertToUppercase();
		String actual = convertToUppercase.convertToUppercase("emmax");
		assertEquals(actual,"0");


	}



}
package com.example.firstapplication;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    EditText uname;
    EditText pass;
    CheckBox rememberCheckBox;
    Button loginButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        uname = findViewById(R.id.txt_u_name);
        pass = findViewById(R.id.txt_pass);
        rememberCheckBox = findViewById(R.id.chk_rem);
        loginButton = findViewById(R.id.btn_login);

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (rememberCheckBox.isChecked()){
                    Toast.makeText(MainActivity.this, "Hello, "+ uname.getText().toString()+ "!", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(MainActivity.this, "Remember Option Not Selected!!", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}

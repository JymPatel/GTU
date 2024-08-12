package com.example.secondapplication;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText urlEditText;
    Button implicitButton, explicitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        urlEditText = findViewById(R.id.text_url);
        implicitButton = findViewById(R.id.button_implicit);
        explicitButton = findViewById(R.id.button_explicit);

        explicitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent exintent = new Intent(MainActivity.this,SecondActivity.class);
                startActivity(exintent);
            }
        });

        implicitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent impintent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://"+ urlEditText.getText().toString()));
                startActivity(impintent);
            }
        });
    }
}